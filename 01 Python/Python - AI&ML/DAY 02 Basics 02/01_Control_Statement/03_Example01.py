age = int(input("Enter Your Age : "))

if(age <=13):
    print("Child")
elif(age>13 and age <18) :
    print("Teenager")
elif(age>=18 and age<60) :
    print("Adult")
else :
    print("Senior Citizen")