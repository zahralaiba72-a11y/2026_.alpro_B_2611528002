#create a program name perluangan_for3_2611538002.py
#create a program for a for loop in python
#variable names are appended with your student number
#this program uses the input() function
ulang= int(input("Enter a number of repetition: "))
jumlah =0
for i in range(1,ulang+1):
   print(i, end=" ")
   jumlah = jumlah +1
   
   if i < ulang:
       print(" +", end=" ")
   else:
       print(" = ", jumlah, end=" ")
       print()
       print("sum =", jumlah)