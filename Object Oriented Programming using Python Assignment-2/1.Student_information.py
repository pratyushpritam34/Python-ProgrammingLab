class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_information(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
    
name = input("Enter the student's name: ")
age = int(input("Enter the student's age: "))
grade = input("Enter the student's grade: ")

student = Student(name, age, grade)


print("Student Information:")
print(student.display_information())
