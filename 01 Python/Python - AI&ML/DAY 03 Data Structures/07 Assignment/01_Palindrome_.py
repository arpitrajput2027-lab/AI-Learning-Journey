str = input("Enter the String : ")

reverse = ""

idx = len(str) -1
for ch in str:
    reverse +=str[idx]
    idx-=1

# print(str,reverse)

if(reverse == str):
    print("String is Palindrome.")
else:
     print("String is NOT a Palindrome.")