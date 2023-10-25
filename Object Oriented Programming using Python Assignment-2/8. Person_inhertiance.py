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

name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")

person = Person(name, age, gender)
print(person.greet())
print(person.introduce())

course = input("Enter your course: ")
student = Student(name, age, gender, course)
print(student.introduce())

subject = input("Enter your subject: ")
teacher = Teacher(name, age, gender, subject)
print(teacher.introduce())
