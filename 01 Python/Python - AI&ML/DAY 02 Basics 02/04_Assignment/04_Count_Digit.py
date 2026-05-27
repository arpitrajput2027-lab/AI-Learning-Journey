n = int(input("Enter the Number : "))
count =0
while(n!=0):
    count+=1
    n = n//10
print("Total Digits in the Number is : ", count)