def Is_prime(n):
    
    for i in range(2, n-1):
        if(n%i==0):
            return False
    return True

n = int(input("Enter the Number : "))

if(n==1):
        print("1 is neither Prime nor Composite")
else:
     ans = Is_prime(n)
     print(ans)
        
