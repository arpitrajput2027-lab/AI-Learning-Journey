import random

num = random.randint(1, 1000)  
original = num

while(1):
        n = int(input("Enter Number Between 1 to 1000 : "))
        if(n>original):
            print("Too High")
        elif(n<original):
            print("Too Low")
        else:
            print("Congratulations! You guessed it right.")

