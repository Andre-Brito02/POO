class Employee:
    def __init__(self, name:str, groos_salary:float, tax:float):
        self._name = name
        self._gross_salary = groos_salary
        self._tax = tax

    def net_salary(self):
        return self._gross_salary - self._tax

    def increase_salary(self, percentage:float):
        self._gross_salary += self._gross_salary/percentage

    def __str__(self):
        return f"{self._name.title()}, $ {self.net_salary():.2f}"

name = input("Name: ")
gross_salary = float(input("Gross Salary: "))
tax = float(input("Tax: "))
emp = Employee(name, gross_salary, tax)

print("Employee: ", emp)

percentage = float(input("Which percentage to increase salary? "))
emp.increase_salary(percentage)

print("Updated data: ", emp)