# Create a file named match_case1.py
# Create a program for match case
# Variable names are appended with the last 4 digits of the student ID (nim), for example: ipk_1234
# This program uses the input() function
# program converts numbers into month names


bulan_8002 = int(input("Enter month number (1 - 12): "))

match bulan_8002:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid number")