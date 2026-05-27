class Employee:
    start_time = "9 AM"
    end_time = "6 PM"

class Techer(Employee):
    def __init__(self, name, salary):
       self.name = name
       self.salary = salary

    def display_info(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")
class Manager(Employee):
    def __init__(self, name, salary, department):
       self.name = name
       self.salary = salary
       self.department = department

    def display_info(self):
        print(f"Manager Name: {self.name}, Salary: {self.salary}, Department: {self.department}")
t1 = Techer("Nisha",50000)
m1 = Manager("Arpit",80000,"IT")
t1.display_info()
m1.display_info()
    
print(f"Techer Working Hours: {t1.start_time} to {t1.end_time}")
print(f"Manager Working Hours: {m1.start_time} to {m1.end_time}")
