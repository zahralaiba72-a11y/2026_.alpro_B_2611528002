# Create a file named bitwise_NIM.py
# Variable names are appended with the last 4 digits of the student ID (example: angka1_1234)
# This program uses the input() function

print("\n==============================")
print("3. BITWISE OPERATOR")
print("==============================")

angka1 = int(input("Enter bitwise number-1: "))
angka2 = int(input("Enter bitwise number-2: "))

print("\nNumbers in decimal and binary form")
print("angka1 =", angka1, "| binary =", bin(angka1))
print("angka2 =", angka2, "| binary =", bin(angka2))

# Bitwise AND
hasil = angka1 & angka2
print("\nBitwise AND (&)")
print(angka1, "&", angka2, "=", hasil)
print("Binary result =", bin(hasil))
print("Binary result (8 bit) =", format(hasil, "08b"))

# Bitwise OR
hasil = angka1 | angka2
print("\nBitwise OR (|)")
print(angka1, "|", angka2, "=", hasil)
print("Binary result =", bin(hasil))
print("Binary result (8 bit) =", format(hasil, "08b"))

# Bitwise XOR
hasil = angka1 ^ angka2
print("\nBitwise XOR (^)")
print(angka1, "^", angka2, "=", hasil)
print("Binary result =", bin(hasil))
print("Binary result (8 bit) =", format(hasil, "08b"))

# Bitwise NOT
hasil = ~angka1
print("\nBitwise NOT (~)")
print("~", angka1, "=", hasil)
print("Binary result =", bin(hasil))
print("Binary result (8 bit) =", format(hasil, "08b"))

# Bitwise left shift
jumlah_geser = int(input("\nEnter the number of bit shifts: "))

hasil = angka1 << jumlah_geser
print("\nBitwise left shift (<<)")
print(angka1, "<<", jumlah_geser, "=", hasil)
print("Binary result =", bin(hasil))
print("Binary result (8 bit) =", format(hasil, "08b"))

# Bitwise right shift
hasil = angka1 >> jumlah_geser
print("\nBitwise right shift (>>)")
print(angka1, ">>", jumlah_geser, "=", hasil)
print("Binary result =", bin(hasil))
print("Binary result (8 bit) =", format(hasil, "08b"))