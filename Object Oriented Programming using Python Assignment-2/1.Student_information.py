class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_information(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

student1 = Student("Munna Bhaiya", 27, "O")
print(student1.display_information())
