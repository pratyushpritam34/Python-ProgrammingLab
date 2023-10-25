class Employee:
    employees = [] 

    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary
        Employee.employees.append(self)

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    @classmethod
    def average_salary(cls):
        total_salary = sum(employee.salary for employee in cls.employees)
        return total_salary / len(cls.employees)


num_employees = int(input("Enter the number of employees: "))
for i in range(num_employees):
    name = input(f"Enter the name of Employee {i + 1}: ")
    id = input(f"Enter the ID of Employee {i + 1}: ")
    salary = float(input(f"Enter the salary of Employee {i + 1}: "))
    employee = Employee(name, id, salary)


employee_index = int(input("Enter the index of the employee to update salary: "))
new_salary = float(input(f"Enter the new salary for {Employee.employees[employee_index].name}: "))
Employee.employees[employee_index].set_salary(new_salary)


avg_salary = Employee.average_salary()
print(f"Average salary of all employees: ${avg_salary:.2f}")
