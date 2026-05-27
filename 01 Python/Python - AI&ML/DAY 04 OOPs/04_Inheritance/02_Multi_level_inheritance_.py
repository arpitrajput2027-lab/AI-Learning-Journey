class Employee:
    start_time = "9 AM"
    end_time = "6 PM"

class AdminStaff(Employee):
    def __init__(self, role):
       self.role = role
    
class HR(AdminStaff):
    def __init__(self, name, salary,role):
       super().__init__(role)
       self.name = name
       self.salary = salary

    def display_info(self):
        print(f"HR Name: {self.name}, Salary: {self.salary}, Role: {self.role}")
        print(f"Working Hours: {self.start_time} to {self.end_time}")

hr1 = HR("Nisha",60000,"HR")
hr1.display_info()