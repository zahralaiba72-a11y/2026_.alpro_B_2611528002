# create a file name multi_if1_2611538002.py
# create a program for conditional statement multi_if1_2611538002
# name a variable with the last 4 digits of nim. example ipk_8002
# This program uses the input() function
age = int(input("input your age: "))
sim = input("Do you already have sim C(y/t):")[0]

if age >= 17 and sim == "y":
    print("you are adult and allowed to drive a car")
    
    if age >=17 and sim != "y":
        print("you are adult but not allowed to drive a car")
        
        if age < 17 and sim == "y":
            print("you are not old enough to have a sim")
            
            if age < 17 and sim != "y":
                print("you are not old enough to drive a car ")
                