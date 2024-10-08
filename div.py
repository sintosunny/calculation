# Function to divide two numbers
def divide_numbers(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

# Example usage
num1 = 10
num2 = 2

result = divide_numbers(num1, num2)
print(f"The division of {num1} by {num2} is: {result}")
