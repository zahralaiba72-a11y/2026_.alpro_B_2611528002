#create a file with name jumlah_genap_2611538002.py
#create a program for loop in python
#variable names are appended with your student number
#this program uses the input() function
loop = int(input("Enter the limit value: "))
sum = 0
for i in range(1, loop + 1):
    if i % 2 == 0:
        print(i, end=" ")
        sum = sum + i
        if i < loop:
            print(" +", end=" ")
        else:
            print(" = ", sum, end=" ")
            print()
print("sum of even numbers =", sum)