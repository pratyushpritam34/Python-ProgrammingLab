from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Bhoo"
class Cat(Animal):
    def sound(self):
        return "meow"

class Cow(Animal):
    def sound(self):
        return "Moo"

animal_type = input("Enter the type of animal (Sheep, Lion, Cat): ")

if animal_type == "Dog":
    animal = Dog()
elif animal_type == "Cat":
    animal = Cat()
elif animal_type == "Cow":
    animal = Cow()
else:
    print("Animal type not recognized.")
    exit()

print(f"The {animal_type} makes the sound: {animal.sound()}")
