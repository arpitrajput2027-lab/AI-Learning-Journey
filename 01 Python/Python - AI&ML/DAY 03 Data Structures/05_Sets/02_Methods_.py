s1 = {1,3,5,7,9,}
s2 = {1,2,3,4,5,6,7,8,9}

s1.add(11) # Adding Element 11 to Set s1
print("After Adding 11 to s1 :",s1)
s1.remove(3)     # Removing Element 3 from Set s1
print("After Removing 3 from s1 :",s1)
s1.pop()          # Removing Random Element from Set s1
print("After Popping an Element from s1 :",s1)
print("Union of s1 and s2 :",s1.union(s2))  # Union of s1 and s2
print("Intersection of s1 and s2 :",s1.intersection(s2)) # Intersection

s3 = {3,7,2,9,5}
print(s3)
s3.clear()  # Clearing all Elements from Set s3
print("After Clearing Set s3 :",s3)