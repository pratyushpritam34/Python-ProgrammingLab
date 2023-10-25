from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Sheep(Animal):
    def sound(self):
        return "Baa"
class Lion(Animal):
    def sound(self):
        return "roar"

class Cat(Animal):
    def sound(self):
        return "Mew"

class Elephant(Animal):
    def sound(self):
        return "trumpet"

animal_type = input("Enter the type of animal (Sheep, Lion, Cat, Elephant): ")

if animal_type == "Sheep":
    animal = Sheep()
elif animal_type == "Lion":
    animal = Lion()
elif animal_type == "Cat":
    animal = Cat()
elif animal_type == "Elephant":
    animal = Elephant()
else:
    print("Animal type not recognized.")
    exit()

print(f"The {animal_type} makes the sound: {animal.sound()}")
