num = [3,7,4,2,5,9,1]

for val in num:
    print(val)

# Search a Targetted Element : X = 5
x = 5
idx =0

for val in num :
    if(val==x):
        print(f"{x} found at Index {idx}")
        break
    idx += 1
