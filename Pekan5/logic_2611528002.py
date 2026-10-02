  # Create a file named logic_NIM.py
  # Variable names are appended with the last 4 digits of the student ID, example: a1_1234
  # This program uses the input() function
  # Logical operator program in Python

  # Entering boolean values
  # Input is not case-sensitive (for uppercase and lowercase letters)
a1 = input("Input boolean value-1 (true/false): ").strip().lower() == "true"
a2 = input("Input boolean value-2 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1)
print("A2 =", a2)

 # Conjunction: evaluates to True if both are True
result = a1 and a2
print("\nConjunction (AND)")
print("A1 and A2 =", result)

 # Disjunction: evaluates to True if at least one is True
result = a1 or a2
print("\nDisjunction (OR)")
print("A1 or A2 =", result)

 # Negation A1: reverses the value of A1
result = not a1
print("\nNegation A1 (NOT)")
print("not A1 =", result)

 # Negation A2: reverses the value of A2
result = not a2
print("\nNegation A2 (NOT)")
print("not A2 =", result)

 # XOR: evaluates to True if both values are different
result = a1 != a2
print("\nExclusive Disjunction (XOR)")
print("A1 XOR A2 =", result)