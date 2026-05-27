num = {
    "Arpit": 1,
    "Rajput" :2,
    "Varun" :3,
    "Kumar" :4,
    "Aryan" :5,
    "Sachin" :6,
    "Bhavneesh" :7,
    "Bhavay" :8,
    "Nishant" :9,
    "Nisha":10
}

while(1):
    print("-------Menu-------")
    choice = input("1. A - Add a student \n2. B - Update marks \n3. C - Search for a student\n4.D - Display all students and marks\n5. Enter Any Key to Exit\n")
    print("\n")
    if(choice == 'A'):
        name = input("Enter Student Name :")
        nums = int(input("Enter the Student's Number : "))
        num.update({name: nums})
        print("Updated Dictionary : ",num)
        break
    elif(choice =='B'):
        naam = input("Enter the Name of Student whose Marks You want to Change :")
        n = int(input("Enter Updated MArks :"))
        num[naam] = n
        print("Updated Dictionary : ",num)
        break
    elif(choice =='C'):
         naam = input("Enter Student Name :")
         print(naam," : ",num[naam])
         break
    elif(choice == 'D'):
        print(num.items())
        break
    else:
        print("Successfuly Exited")
        break

    


