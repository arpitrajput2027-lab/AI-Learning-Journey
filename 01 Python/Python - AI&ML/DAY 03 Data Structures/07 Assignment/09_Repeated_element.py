# Given a list, print all elements that appear more than once in the list

list1 = [1,2,3,3,4,5,6,6,7,8,8,9]

setl = set()

for i in range(len(list1)):
    if(list1[i] in setl):
        print(list1[i])
    else:
        setl.add(list1[i])

print(setl)