# create a program file name multi_if2_nim.py
# create a program for conditional if statement.
# name a variable with the last 4 digits of nim. example ipk_8002
# This program uses the input() function
# program calculates the shopping discount

# Input from user
total_purchase = float(input("Enter your total purchase amount(Rp): ")) 

# Input status member(check wether user type y or ya)
input_member = input("Are you a member (y/t): ").strip().lower()
is_member = input_member in ["y", "ya"]

# input promo code status (check wether user type y or ya)
input_promo = input("Is the promo code valid(y/t): ").strip().lower()
code_promo_valid = input_promo in ["y", "ya"]

total_discount_persentage = 0
# multi_if seperated: Each condition is checked independently
# Discounts can be stacked (accumulated) if it meets several conditions at once

if total_purchase > 1000000:
    total_discount_persentage += 10  # Large purchase discount

if is_member:
    total_discount_persentage += 5   # Member discount

if code_promo_valid:
    total_discount_persentage += 15  # Voucher discount

# Calculate discount amount and total payment
nominal_discount = total_purchase * (total_discount_persentage / 100)
total_payment = total_purchase - nominal_discount

# Output results
print("\n--- Payment Details ---")
print(f"Total Discount : {total_discount_persentage}% (Rp {nominal_discount:,.0f})")
print(f"Total Payment  : Rp {total_payment:,.0f}")

print(f"Total discount you get: {total_discount_persentage}%")
# Output: Total discount you get: 30% if purchase > 1 million, member, and valid promo code