info = [
    ("Arpit","OOPs"),
    ("Rajput","Python"),
    ("Varun","OOPs"),
    ("Kumar","Data Science"),
    ("Aryan","Python"),
    ("Sachin","Data Science"),
    ("Bhavneesh","AI"),
    ("Bhavay","AI"),
    ("Nishant","DSA in JAVA"),
    ("Ankit","DBMS"),  
    ("Bhavay","OOPs"),
    ("Arpit","AI"),
    ("Nishant","AI"),
    ("Aryan","DSA in JAVA"),
]
for name , courses in info:
    print(name,courses)

# Make Dictionary : (student : Set of Courses)

dic = {}
for name , courses in info:
    if(dic.get(name)==None):
        dic.update({name :set()})
        dic[name].add(courses)
    else:
        dic[name].add(courses)
print("Student Course Dictionary :")
print(dic)
# Mja Aaya :)
    
