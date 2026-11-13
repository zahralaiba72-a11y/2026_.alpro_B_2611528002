username = input("Username: ")
 
# Check the rules in a safe order and print the first rule that fails.
# Messages:
#   "Invalid: at least 5 characters"
#   "Invalid: letters and digits only"
#   "Invalid: must start with a letter"
#   "Valid"
# Check the rules in a safe order and print the first rule that fails.
if len(username) < 5:
    print("Invalid: at least 5 characters")
elif not username.isalnum():
    print("Invalid: letters and digits only")
elif not username[0].isalpha():
    print("Invalid: must start with a letter")
else:
    print("Valid")
# PART B: A NIM is valid if it has 10 characters and all of them are digits
nim = input("Your NIM: ")

# Check if the NIM has exactly 10 characters and all of them are digits
if len(nim) == 10 and nim.isdigit():
    # first two digits for intake year (20xx)
    xx = nim[:2]
    print(f"Valid, intake year 20{xx}")
else:
    print("Invalid NIM code")

# 1. Your NIM without the last digit
nim_without_last = nim[:-1]
print(f"Without last digit ({nim_without_last}):")
if len(nim_without_last) == 10 and nim_without_last.isdigit():
    xx = nim_without_last[:2]
    print(f"Valid, intake year 20{xx}")
else:
    print("Invalid NIM code")

# 2. Your NIM without the last digit, plus the letter A
nim_with_a = nim[:-1] + "A"
print(f"Without last digit + 'A' ({nim_with_a}):")
if len(nim_with_a) == 10 and nim_with_a.isdigit():
    xx = nim_with_a[:2]
    print(f"Valid, intake year 20{xx}")
else:
    print("Invalid NIM code")
    