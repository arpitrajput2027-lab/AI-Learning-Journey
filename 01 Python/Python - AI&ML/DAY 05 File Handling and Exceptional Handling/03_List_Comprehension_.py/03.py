listx = [2,-6,9,-3,-0,4,8,-1]

list1 = [ listx[i] if listx[i]>=0  else 0 for i in range(len(listx))]
list2 = [ val if val>=0  else 0 for val in listx]
print(list2)
print(list2)