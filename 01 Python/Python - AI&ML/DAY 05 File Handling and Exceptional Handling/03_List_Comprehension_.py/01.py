# Loop Method
sq = []
for i in range(11):
    sq.append(i*i)
print(sq)


# Same with List Comprehension (This Basically Replacement of Loop)

square = [i*i for i in range(11)]
print(square)