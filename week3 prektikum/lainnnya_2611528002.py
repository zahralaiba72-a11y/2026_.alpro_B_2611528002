# Create a file named lainnya_NIM.py (others_NIM.py)
# Variable names are appended with the last 4 digits of the student ID, example: number1_1234            # This program uses the input() function
# Membership and identity operator program

print("================================")
print("1. MEMBERSHIP OPERATOR")
print("================================")

# Input several data separated by commas
input_data = input("Enter several numbers, separate with commas: ")

# Convert input into an integer list
data = [int(number.strip()) for number in input_data.split(",")]

search_value = int(input("Enter the number you want to search for: "))

# Operator in
result = search_value in data
print("\nMembership operator IN")
print(search_value, "in", data, "=", result)

# Operator not in
result = search_value not in data
print("\nMembership operator NOT IN")
print(search_value, "not in", data, "=", result)

print("\n================================")
print("2. IDENTITY OPERATOR")
print("================================")

# objek1 uses the list from user input
objek1 = data

# objek2 refers to the same object as objek1
objek2 = objek1

# objek3 has the same contents, but is a new object
objek3 = data.copy()

print("objek1 =", objek1)
print("objek2 =", objek2)
print("objek3 =", objek3)

# Operator is
result = objek1 is objek2
print("\nIdentity operator IS")
print("objek1 is objek2 =", result)

# Operator is not
result = objek1 is not objek3
print("\nIdentity operator IS NOT")
print("objek1 is not objek3 =", result)

# Comparing identity and value
print("\nComparison of identity and value")
print("objek1 is objek3 =", objek1 is objek3)
print("objek1 == objek3 =", objek1 == objek3)