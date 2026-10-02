# Create a file named assignment_NIM.py
# Variable names are appended with the last 4 digits of the student ID, example: number1_1234
# This program uses the input() function
# The entered value will be converted to an integer data type
# Assignment operator program in Python

number1 = int(input("Input number-1: "))
number2 = int(input("Input number-2: "))

print("\nInitial value of number1 =", number1)
print("Value of number2 =", number2)

# Standard assignment
result = number1
print("\nStandard assignment (=)")
print("Result =", result)

# Addition assignment
result = number1
result += number2
print("\nAddition assignment (+=)")
print("Result =", result)

# Subtraction assignment
result = number1
result -= number2
print("\nSubtraction assignment (-=)")
print("Result =", result)

# Multiplication assignment
result = number1
result *= number2
print("\nMultiplication assignment (*=)")
print("Result =", result)

# Division, integer division, and modulo assignment
if number2 != 0:
    result = number1
    result /= number2
    print("\nDivision assignment (/=)")
    print("Result =", result)
    # Additional operator
    result = number1
    result //= number2
    print("\nInteger division assignment (//=)")
    print("Result =", result)
    result = number1
    result %= number2
    print("\nModulo assignment (% =)")
    print("Result =", result)
else:
    print("\nDivision cannot be performed.")
    print("The second number cannot be 0.")

# Additional operator: exponentiation assignment
result = number1
result **= number2
print("\nExponentiation assignment (**=)")
print("Result =", result)