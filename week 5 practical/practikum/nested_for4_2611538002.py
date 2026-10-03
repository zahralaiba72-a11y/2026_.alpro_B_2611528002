# Create a file named nested_for4_NIM.py
# Create a program for a for loop in Python
# Variable names are appended with the last 4 digits of the student ID (NIM), for example: ulang_1234
# This program uses the input() function

height = int(input("Enter the pattern height (even number, e.g., 10): "))

if height % 2 != 0:
    print("Height must be an even number!")
else:
    a = height
    c = a
    width = (2 * height) - 2

    for i in range(1, height + 1):
        b = c + 1

        for j in range(1, width + 1):

            # Top and bottom rows
            if i == 1 or i == height:
                if j == 1 or j == width:
                    print("#", end="")
                else:
                    print("=", end="")
                    # Body row
    else:
        if j == 1 or j == width:
            print("|", end="")
        else:
            if j == c:
                print("<", end="")
            elif j == b:
                print(">", end="")
            elif j == (width - c):
                print("<", end="")
            elif j == (width - c + 1):
                print(">", end="")
            elif j > b and j < (width - c):
                print(".", end="")
            else:
                print(" ", end="")

print()

# Original Java logic
a -= 2

if a <= 0:
    c = (-a) + 2
else:
    c = a