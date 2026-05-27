# class student:
#     def __init__(self,name,cgpa):
#         self.name = name
#         self.cgpa = cgpa

#     def get_cgpa(self):
#         return self.cgpa
    

# s1 = student("Arpit", 9.1)
# s2 = student("Nisha", 8.5)
# print(s1.name , s1.get_cgpa())  # Arpit 9.1
# print(s2.name , s2.get_cgpa())  # Nisha 8.5



print("\n--------------------\n")

class student:
   

    def __init__(self):   # Default Constructor
        print("In Python Multiple Constructor are NOT Allowed")
   # But still if we write Multiple Construtor , then Last one will be executes

    def __init__(self,name,cgpa): # Parameterized Constructor
            self.name = name
            self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa
    
    
s1 = student("Arpit", 9.1)
s2 = student("Nisha", 8.5)
print(s1.name , s1.get_cgpa())  # Arpit 9.1
print(s2.name , s2.get_cgpa())  # Nisha 8.5