from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        self._members = []

  
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        """
        Agrega un nuevo miembro a la familia.
        Si no se proporciona un ID, se genera uno automáticamente.
        """
        if 'id' not in member:  
            member['id'] = self._generateId()
        member['last_name'] = self.last_name  
        self._members.append(member)
        return member  

    def delete_member(self, id):
        """
        Elimina un miembro de la familia por su ID.
        """
        self._members = [member for member in self._members if member['id'] != id]
        return {"message": f"Member with ID {id} deleted"}

    def update_member(self, id, updates):
        """
        Actualiza un miembro de la familia por su ID.
        """
        for member in self._members:
            if member['id'] == id:
                member.update(updates)  
                return member  
        return {"error": "Member not found"}  

    def get_member(self, id):
        """
        Obtiene un miembro de la familia por su ID.
        """
        for member in self._members:
            if member['id'] == id:
                return member
        return {"error": "Member not found"}  

    
    def get_all_members(self):
        return self._members

jackson_family = FamilyStructure('Jackson')

initial_members = [
    {"first_name": "John", "age": 33, "lucky_numbers": [7, 13, 22]},
    {"first_name": "Jane", "age": 35, "lucky_numbers": [10, 14, 3]},
    {"first_name": "Jimmy", "age": 5, "lucky_numbers": [1]}
]

for member in initial_members:
    jackson_family.add_member(member)


if __name__ == "__main__":
    print("Miembros iniciales:", jackson_family.get_all_members())
