class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        return f"Hello, my name is {self.name}."

    def introduce(self):
        return f"My name is {self.name}, and I am {self.age} years old."

class Student(Person):
    def __init__(self, name, age, gender, course):
        super().__init__(name, age, gender)
        self.course = course

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old, and I am studying {self.course}."

class Teacher(Person):
    def __init__(self, name, age, gender, subject):
        super().__init__(name, age, gender)
        self.subject = subject

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old, and I teach {self.subject}."

person1 = Person("Mohan", 25, "Male")
student1 = Student("Shyam", 20, "Male", "Science")
teacher1 = Teacher("Radhe", 35, "Female", "Social Science")

print(person1.greet())
print(person1.introduce())

print(student1.greet())
print(student1.introduce())

print(teacher1.greet())
print(teacher1.introduce())
