class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

def create_employee(details):
    new_employee = Employee(details['name'], details['age'], details['salary'])
    return new_employee

name = input("Enter the name of the employee: ")
age = int(input("Enter the age of the employee: "))
salary = int(input("Enter the salary of the employee: "))

details = {
    'name': name,
    'age': age,
    'salary': salary
}

employee_instance = create_employee(details)
print(f"Details of the employee: Name - {employee_instance.name}, Age - {employee_instance.age}, Salary - {employee_instance.salary}")