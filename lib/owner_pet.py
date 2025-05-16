class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.name = name
        self._pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
    
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet):
        if pet in Pet.PET_TYPES:
            self._pet_type = pet
        else:
            raise Exception(f"Invalid pet type: {pet}")
        


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("Only Pet instances can be added")
        
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)