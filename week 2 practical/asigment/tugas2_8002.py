# File Name: tugas2_1234.py
# Replace '1234' with the last 4 digits of your actual NIM

# 1. Constant Implementation (Passing Threshold)
PASSING_SCORE_8002 = 75.0

print("=== ALPRO PRACTICUM REGISTRATION SYSTEM 2026 ===")

# 2. String, Char, & Multi-line Address Inputs
student_name_8002 = str(input("Enter Student Name : "))
gender_8002 = str(input("Enter Gender (L/P): "))

print("Enter Residential Address (Multi-line format):")
address_8002 = """Jl. Kampus Unand,
Kecamatan Pauh,
Kota Padang"""
print(address_8002)

# 3. Numeric Inputs & Type Casting
age_8002 = int(input("Enter Age : "))
initial_score_8002 = float(input("Enter Initial Test Score : "))

# 4. Complex Number Token ID
token_id_8002 = complex(100, 3)

# 5. Boolean Validation Status
is_passed_8002 = initial_score_8002 >= PASSING_SCORE_8002

# 6. Display Output with Type Checking
print("\n=== PRACTICUM DATA & CHECK RESULTS ===")
print(f"Student Name   : {student_name_8002} | Type: {type(student_name_8002)}")
print(f"Gender         : {gender_8002} | Type: {type(gender_8002)}")
print(f"Address        :\n{address_8002} | Type: {type(address_8002)}")
print(f"Age            : {age_8002} years old | Type: {type(age_8002)}")
print(f"Initial Score  : {initial_score_8002} | Type: {type(initial_score_8002)}")
print(f"Signal Token ID: {token_id_8002} | Type: {type(token_id_8002)}")
print(f"Passed Status  : {is_passed_8002} | Type: {type(is_passed_8002)}")