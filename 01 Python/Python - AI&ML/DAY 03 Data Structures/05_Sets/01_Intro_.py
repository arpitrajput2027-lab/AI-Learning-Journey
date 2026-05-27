s = {1, 2, 3, 4, 5,5,5}

print(s)
print(type(s))
print(len(s))

# Sets are Unordered and Unindexed
# Duplicates Not Allowed in Sets
# Mutable : Updation Allowed

s.add(6)
print(s)

# Empty Set
empty_set_x = {}
empty_set = set()

print(type(empty_set_x))  # dict
print(type(empty_set))    # set
if(87 in s):
    print("Present")
else:
    print("NOT Present")