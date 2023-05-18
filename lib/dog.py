#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed
dog1 = Dog("Fido", "Dalmatian")
print(dog1.name)   
print(dog1.breed)  

dog2 = Dog("Max")
print(dog2.name)   
print(dog2.breed)  




pass