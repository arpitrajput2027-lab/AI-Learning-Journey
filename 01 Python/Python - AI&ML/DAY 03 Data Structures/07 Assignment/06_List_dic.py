words = ["apple","banana","kiwi","cherry","mango"]

#Create a dictionary that maps each word to its length.
dic = {}
for i in range(len(words)):
    dic.update({words[i] : len(words[i])})
print(dic)
