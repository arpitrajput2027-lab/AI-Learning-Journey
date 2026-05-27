# Write a program to check whether two lists share no common elements.

list01 = [1,2,3,4,5]
list02 = [6,7,8,8,17]

set1 = set(list01)
set2 = set(list02)

set3 = set1.intersection(set2)

if(set3 == set()):
    print("share no common elements")
else :
     print("share  common elements")