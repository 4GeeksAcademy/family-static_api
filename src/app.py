"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# GET all members
@app.route('/members', methods=['GET'])
def handle_members():
        members = jackson_family.get_all_members()
        
        return jsonify(members), 200

# POST a new member
@app.route('/member', methods=['POST'])
def handle_member_post():
    try:
        data = request.json
        if 'first_name' not in data or 'age' not in data or 'lucky_numbers' not in data:
            return jsonify({"message": "Incomplete request. Missing fields"}), 400
        
        new_member = jackson_family.add_member(data)
        return jsonify(new_member), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 400


# GET, POST, and DELETE a specific member
@app.route('/member/<int:member_id>', methods=['GET', 'DELETE'])
def handle_member(member_id):
    try:
        if request.method == 'GET': 
            member = jackson_family.get_member(member_id)
            if member is None:
                return jsonify({"message": "Member not found"}), 404
            return jsonify(member), 200

        if request.method == 'DELETE':
            deleted = jackson_family.delete_member(member_id)
            if deleted:
                return jsonify({"done": True}), 200 
            else:
                return jsonify({"message": "Member not found"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 400

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
