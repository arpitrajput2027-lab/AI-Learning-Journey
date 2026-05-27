def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
    
a = int(input("Enter the First Operand :"))
b = int(input("Enter the Second Operand :"))
operation = input("Enter the Operation (+, -, *, /) :")

result = calculator(a, b, operation)
print("Result:", result)