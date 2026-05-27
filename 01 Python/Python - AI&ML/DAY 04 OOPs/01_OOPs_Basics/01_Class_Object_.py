class student:
    subject = "AI & ML"
    year = "4th Year"
    college = "IIT Roorkee"

stu1 = student()
print(stu1) # <__main__.student object at (memory address)>
print(type(stu1))  # <class '__main__.student'>
print(stu1.subject , stu1.year , stu1.college)

s = set()
print(type(s))  # class set