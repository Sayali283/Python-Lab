#Implement object-oriented programming concepts such as inheritance, polymorphism, and abstraction to develop Python applications.
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    def display(self):
        print("Employee:", self.name)
        print("Salary:", self.calculate_salary())


class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, hours, hourly_rate):
        super().__init__(name)
        self.hours = hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours * self.hourly_rate


employees = [
    FullTimeEmployee("Amit", 40000),
    PartTimeEmployee("Neha", 80, 250)
]

for employee in employees:
    employee.display()
    print()
