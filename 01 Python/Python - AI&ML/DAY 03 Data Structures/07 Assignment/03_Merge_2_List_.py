n = int(input("Enter the Number of Element in List 1 : "))
m = int(input("Enter the Number of Element in List 1 : "))

list01 = []
list02 = []
print("Enter the Elements of First List :" )
for i in range(n):
    list01+=input("Enter Element : ")

print("Enter the Elements of Second List :" )
for i in range(m):
    list02+=input("Enter Element : ")

print("List 1 : ",list01)
print("List 2 : ",list02)

list03 = list01 + list02
list03.sort()
print("Sorted Merged List : ",list03)

