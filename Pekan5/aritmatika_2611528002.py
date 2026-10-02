#create a file name arithmetic_NIM.py
#create a program for arithmetic operators in python
# Variable names are appended with the last 4 digits of student nim
#THis program uses the input() function
#the entered value will be converted to an integer data type

number1 = int(input("input number - 1:  "))
number2 = int(input("input number - 2:  "))

#Addition
result = number1 + number2
print("\nAddition Operator")
print("Result =", result)

#Subtraction
result = number1 - number2
print("\nSubtraction Operator")
print("Result =", result)

#Multiplication
result = number1 * number2
print("\nMultiplication Operator")
print("Result =", result)

#Division integer division, and modulo
if number2 != 0:
    result = number1 / number2
    print("\nDivision Operator")
    print("Result =", result)
       
    result = number1 // number2
    print("\n Integer Division Operator")
    print("Result =", result)
              
    result = number1 % number2
    print("\nModulo Operator")
    print("Result =", result)
else:
    print(" The second number cannot be 0")
    result = number1 ** number2 
    print("\nExponentiation Operator")
    print("Result =", result)  
           



