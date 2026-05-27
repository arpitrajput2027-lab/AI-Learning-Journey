class student:
    college_name = "CGC"   # Class Attribute
    nirf_rank = 125

    def __init__(self, name, cgpa):  
        self.name = name     # Instance Attribute
        self.cgpa = cgpa
        self.nirf_rank = 130 

stu1 = student("Arpit",9.8)

print(student.college_name)  # Accessing Class Attribute using Class Name
print(stu1.college_name)     # Accessing Class Attribute using Object

# print(student.name) -->> NOT ALLOWED
print(stu1.name)             # Accessing Instance Attribute using Only  Object

print("--------------------")
print(stu1.nirf_rank)        # 130  Accessing Instance Attribute using Object
print(student.nirf_rank)     # 125  Accessing Class Attribute using Class Name

