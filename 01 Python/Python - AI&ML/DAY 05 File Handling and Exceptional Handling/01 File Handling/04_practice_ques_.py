f = open("practice.txt","r")

lineCount = 1

flag = False

for line in f:
    if(" Python " in line):
        flag = True
        break
    lineCount += 1

if (flag == True):
    print("The word 'Python' was  found in the file.\n At line number:", lineCount)   
else:
    print("The word 'Python' was NOT found in the file.")

f.close()