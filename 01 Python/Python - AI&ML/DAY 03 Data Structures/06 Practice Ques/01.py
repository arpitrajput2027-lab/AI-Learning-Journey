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
]
# Find the Unique Subjects :

course_set = set()

# for i in range(len(info)):
#     course_set.add(info[i][1])

for tup in info:
    course_set.add(tup[1])

print("Unique Courses Offered:")
print(course_set)