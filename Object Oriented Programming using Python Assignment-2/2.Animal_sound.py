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

cat = Cat()
print(cat.sound())

