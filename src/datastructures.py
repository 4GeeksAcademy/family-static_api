
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {'id': self._generateId(), 'first_name': 'John', 'last_name': 'Jackson', 'age': 33, 'lucky_numbers': [7, 13, 22]},
            {'id': self._generateId(), 'first_name': 'Jane', 'last_name': 'Jackson', 'age': 35, 'lucky_numbers': [10, 14, 3]},
            {'id': self._generateId(), 'first_name': 'Jimmy', 'last_name': 'Jackson', 'age': 5, 'lucky_numbers': [1]}
        ]

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member['last_name'] = self.last_name
        self._members.append(member)
        return member

    def delete_member(self, id):
        member_to_delete = [member for member in self._members if member['id'] == id]
        if member_to_delete:
            self._members.remove(member_to_delete[0])
            return member_to_delete[0]
        else:
            return None

    def update_member(self, id, new_info):
        member_to_update = [member for member in self._members if member['id'] == id]
        if member_to_update:
            member_to_update[0].update(new_info)
            return member_to_update[0]
        else:
            return None

    def get_member(self, id):
        member_to_get = [member for member in self._members if member['id'] == id]
        return member_to_get[0] if member_to_get else None

    def get_all_members(self):
        return self._members

# Initialize the class
jackson_family = FamilyStructure('Jackson')
