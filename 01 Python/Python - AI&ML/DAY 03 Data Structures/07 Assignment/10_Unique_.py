# Ask the user for a string and print:
#  All unique characters & 
# The count of unique characters

str = input("Enter the String : ")

setl = set()

count = 0
for i in range(len(str)):
    if(str[i] in setl):
        print(str[i])
    else:
        setl.add(str[i])
        count+=1
print("All unique characters : ")
print(setl)
print("The count of unique characters : ",count,len(setl))