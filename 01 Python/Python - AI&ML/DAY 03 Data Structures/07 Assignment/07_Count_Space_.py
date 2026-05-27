# Write a program that takes a string from the
# user and prints the number of spaces in the string.

str = input("Enter teh String : ")
count = 0
for i in range(len(str)):
    if(str[i]==' '):
        count+=1
print("Number of Spaces : ",count)