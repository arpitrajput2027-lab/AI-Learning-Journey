# try block is which contains the code that may raise an exception.
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2

# except block is used to handle the exception.
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid integers.")

else:
    print("The result is:", result)

# finally block of code is always executed.
finally:
    print("finally block of code is always executed.")
    print("Execution completed.")