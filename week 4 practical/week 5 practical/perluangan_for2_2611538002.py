# Create a file named perulangan_for2_NIM.py
# Create a program for a for loop in Python
# Variable names are appended with the last 4 digits of the student ID (NIM), for example: ulang_1234
# This program uses the input() function

ulang = int(input("Enter the number of repetitions: "))
print("Repetition from 0 to", ulang-1)
for i in range(ulang):
    print(i, end=" ")
print()
print("Repetition from 1 to", ulang)
for i in range(1, ulang+1):
    print(i, end=" ")