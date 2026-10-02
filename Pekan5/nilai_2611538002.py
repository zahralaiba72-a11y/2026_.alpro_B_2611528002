# Create a file named nilai_nim.py
# Create a program for nested if
# Variable names are appended with the last 4 digits of the student ID (nim), for example: ipk_1234
# This program uses the input() function
# program converts numeric grades to letter grades

nilai = int(input("Enter numeric grade= "))

if nilai >= 81:
    print("A")
elif nilai >= 70:
    print("B")
elif nilai >= 60:
    print("C")
elif nilai >= 50:
    print("D")
else:
    print("E")