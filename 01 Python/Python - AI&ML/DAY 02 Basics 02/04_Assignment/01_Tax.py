salary = int(input("Enter Your Salary : "))

if(salary<0):
    print("Invalid Salary")
if(salary<30000):
    print("Tax : ",salary*0.05)
elif(salary>=30000 and salary<=70000):
    print("Tax : ",salary*0.15)
else:
    print("Tax : ",salary*0.25)