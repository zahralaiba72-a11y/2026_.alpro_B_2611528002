# create a file name if_elif_else1_nim.py
# create a programfor conditional statement if
# variable name s are appended with the last 4 digits of nim. example ipk_8002
# this program uses a input() function
age = int(input("input your age: "))
license = input("Do you already have a driving license (y/t):")[0]

if age >= 17 and license == "y":
    print("you are adult and allowed to drive a car")
elif age >= 17 and license != "y":
    print("you are adult but  not allowed to drive a car")
elif age < 17 and license == "y":
    print("you are not old enough to have a driving license")
else:
    print("you are not old enough to drive a car ")
    print(" Program finished.")
    
    