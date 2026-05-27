tup = (1,2,3,4,5,6,7,8,9,0)
tup01 = ()
tup02 = ()

for i in range(len(tup)):
    if(tup[i]%2==0):
        tup01 += (tup[i],)
    else:
        tup02 += (tup[i],)

print(tup01)
print(tup02)