# Create a file named perbandigan/comparison_NIM.py
# Variable names are appended with the last 4 digits of the student ID, example: number1_1234
# This program uses the input() function
# The entered value will be converted to an integer data type
# Comparison operator program in Python

number1 = int(input("Input number-1: "))
number2 = int(input("Input number-2: "))

# Greater than
result = number1 > number2
print("\nGreater than operator")
print("number1 > number2 =", result)

# Less than
result = number1 < number2
print("\nLess than operator")
print("number1 < number2 =", result)

# Greater than or equal to
result = number1 >= number2
print("\nGreater than or equal to operator")
print("number1 >= number2 =", result)

# Less than or equal to
result = number1 <= number2
print("\nLess than or equal to operator")
print("number1 <= number2 =", result)

# Equal to
result = number1 == number2
print("\nEqual to operator")
print("number1 == number2 =", result)

# Not equal to
result = number1 != number2
print("\nNot equal to operator")
print("number1 != number2 =", result)

# Additional: chained comparison in Python
result = 0 < number1 < 100
print("\nChained comparison")
print("0 < number1 < 100 =", result)

result = 0 < number2 < 100
print("0 < number2 < 100 =", result)