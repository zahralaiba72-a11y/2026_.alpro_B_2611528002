# create a file named constant_2611528002.py
# this program uses a constant to calculate the area of circle
# variable names are appended with the last 4 digits of student ID, exam name_123
from typing import Final
PI_8002: Final = 3.14 #this is a constant variable
print("pi: %f" % PI_8002) #this is a string and we executed pi
radius_8002 = float(input("Enter the radius value: "))#this is a variable if numeric
area_8002 = PI_8002 * radius_8002 * radius_8002 #this is a variable if numeric
print("The area of the circle with radius %.2f is: %.2f" % (radius_8002, area_8002)) #this is a string and we executed the area of the circle