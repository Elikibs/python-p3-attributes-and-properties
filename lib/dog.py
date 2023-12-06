#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self):
        self._name = None
        self._breed = None

    # name propert
    def get_name(self):
        return self._name
    
    # breed property
    def get_breed(self):
        return self._breed

    # Setting name 
    def set_name(self, name_value):
        if not isinstance(name_value, str) or not (1 <= len(name_value) <= 25):
            print("Name must be a string between 1 and 25 characters.")
        else:
            self._name = name_value
    def set_breed(self, breed_value):
        if breed_value not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = breed_value

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)

# Example usage:
my_dog = Dog()
my_dog.name = "Elisha KIbet"
print(my_dog.name)
my_dog.breed = "Pugi"
print(my_dog.breed)