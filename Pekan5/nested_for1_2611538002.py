#create a program name neasted_for1_2611538002.py
#create a program for a nested for loop in python
#variable names are appended with your student number
limit = int(input("Enter the limit value: "))
for line in range(1, limit+1):
    for j in range(1, line+1):
        print("*", end=" ")
    print(line)