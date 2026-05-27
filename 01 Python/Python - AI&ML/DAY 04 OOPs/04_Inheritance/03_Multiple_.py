class Teacher:
    def __init__(self,salary, subject):
       
        self.salary = salary
        self.subject = subject

class Student:
    def __init__(self, grade):
        self.grade = grade

class TeachingAssistant(Teacher, Student):
    def __init__(self, name, salary, subject, grade):
        super().__init__(salary, subject)
        Student.__init__(self, grade)
        self.name = name

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Subject: {self.subject}, Grade: {self.grade}")

ta1 = TeachingAssistant("Alex", 40000, "Mathematics", "A")
ta1.display_info()