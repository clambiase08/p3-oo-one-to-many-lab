class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if self.check_type(pet_type):
            self.name = name
            self.owner = owner
            self.pet_type = pet_type
            Pet.all.append(self)
        else:
            raise Exception

    @classmethod
    def check_type(cls, pet_type):
        return pet_type in cls.PET_TYPES


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception
        else:
            pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
