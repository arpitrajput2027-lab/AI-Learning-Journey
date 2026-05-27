class student:
    def __init__(self):
        print("Constructor Called...")

stu1 = student()  # Constructor Called...
stu2 = student()  # Constructor Called...


print("\n--------------------\n")
    
    
class teacher:
    def __init__(self,name, subject):
        self.name = name
        self.subject = subject

t1 = teacher("Manpreet_Mam", "Mathematics")
t2 = teacher("Ripple_Mam", "BEE")  
print(t1.name , t1.subject)  # Manpreet_Mam Mathematics
print(t2.name , t2.subject)  # Ripple_Mam BEE