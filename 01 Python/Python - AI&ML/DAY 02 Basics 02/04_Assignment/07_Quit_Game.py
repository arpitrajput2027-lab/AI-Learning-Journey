

while(1):
    num = input("Enter the Number for Playing the Game :")
    if(num=="Quit" or num=="quit" or num=="QUIT"):
        print("You have Quit the Game")
        break
    elif(num!="Quit"):
        continue
    else :
        if(int(num)>0 or int(num)<=0):
            print(num)
       