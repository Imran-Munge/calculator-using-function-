

def sum(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a / b    
def modulus(a,b):
    return a % b
print("_______________________________________\n")
print("Welcome to the calculator\n")
print("_______________________________________\n")
print("enter exit to exit the calculator\n")
print("Enter the two numbers to be calculated : ")
a = int(input("a: "))
b = int(input("b: "))
input_operation = input("Enter operation (sum, subtract, multiply, divide,modulus, exit ): ").strip().lower()
while input_operation != "exit":
    if input_operation == "sum":
        print("Result:", sum(a, b))
    elif input_operation == "subtract":
        print("Result:", subtract(a, b))
    elif input_operation == "multiply":
        print("Result:", multiply(a, b))    
    elif input_operation == "divide":
        print("Result:", divide(a, b))
    elif input_operation == "modulus":
        print("Result:", modulus(a, b))
    else:
        print("Invalid operation.")
    input_operation = input("Enter operation (sum, subtract, multiply, divide,modulus, exit): ").strip().lower()
print("Exiting the calculator.")