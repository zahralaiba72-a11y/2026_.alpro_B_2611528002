#create a program name nested_for3_2611538002.py
#create a program for a nested for loop in python
#variable names are appended with your student number
#this program uses the input() function
limit = int(input("Enter the limit value: "))
for i in range(1, limit+1):
    for j in range(limit+1):
        print(i+j, end=" ")
    print()#move to the next line