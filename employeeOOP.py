class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def calculate_total_salary(self, months):
        total_salary = self.salary * months
        return total_salary

    def is_eligible_to_work(self):
        return self.age >= 21


def main():
    name = input("Enter the name of the employee: ")
    age = int(input("Enter the age of the employee: "))
    salary = float(input("Enter the monthly salary of the employee: "))
    
    employee = Employee(name, age, salary)
    
    total_salary = employee.calculate_total_salary(12)
    eligibility = employee.is_eligible_to_work()

    print(f"\nEmployee Details:")
    print(f"Name: {employee.name}")
    print(f"Age: {employee.age}")
    print(f"Monthly Salary: {employee.salary}")
    print(f"Total Salary for one year: {total_salary}")

    if eligibility:
        print("The employee is eligible to work.")
    else:
        print("The employee is not eligible to work.")


if __name__ == "__main__":
    main()