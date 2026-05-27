a = 2
b = 4
sum = a+b

# Method 01 : format()
# Normal Formating
print("Sum of {} and {} is {}".format(a,b,sum))
print("Sum of {} and {} is {}".format(a,b,a+b))
print("I am Learning{}".format("Python"))

# Index Based Formating
print("Sum of {1} is {0} is {2}".format(a,b,sum))

# ValueBased Formating
print("Value of Variables {a} and {b}".format(a=6,b=9))


# Method 02 : f-Strings (Python 3.6+)
print(f"Sum of {a} and {b} is {sum}")
