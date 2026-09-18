# assignment3_2611528002.py
# Week 3 Assignment - Algorithms and Programming Practicum 2026

# --- 1. USER INPUT & DATA TYPES ---
name_1234 = input("Enter Customer Name: ")
status_1234 = input("Enter Customer Status (member/non-member): ").strip().lower()
total_1234 = float(input("Enter Total Purchase: "))
item_count_1234 = int(input("Enter Number of Items: "))
promo_code_1234 = input("Enter Promo Code: ").strip().upper()

# List of available promo codes
promo_list_1234 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

# --- 2. MEMBERSHIP OPERATORS ---
# Check if the promo code exists in the list
valid_promo_1234 = promo_code_1234 in promo_list_1234        # 'in' operator
invalid_promo_1234 = promo_code_1234 not in promo_list_1234  # 'not in' operator

# --- 3. COMPARISON OPERATORS ---
# Evaluates expressions into boolean True or False values
min_purchase_met_1234 = total_1234 >= 200000  # '>=' operator
min_items_met_1234 = item_count_1234 >= 3      # '>=' operator
is_member_1234 = status_1234 == "member"      # '==' operator

# --- 4. LOGICAL OPERATORS ---
# Combines multiple conditions using and, or, and not
gets_discount_1234 = is_member_1234 and min_purchase_met_1234  # 'and' operator
gets_promo_1234 = (min_items_met_1234 or valid_promo_1234) and not (total_1234 < 50000)  # 'or', 'not'

# --- 5. ARITHMETIC OPERATORS ---
# Calculate discount amount, final payment, average item price, and remainder
discount_rate_1234 = 0.10 if gets_discount_1234 else 0.0
discount_amount_1234 = total_1234 * discount_rate_1234  # '*' multiplication operator
final_payment_1234 = total_1234 - discount_amount_1234  # '-' subtraction operator
avg_item_price_1234 = total_1234 / item_count_1234      # '/' division operator
item_remainder_1234 = item_count_1234 % 2              # '%' modulus operator

# --- 6. ASSIGNMENT OPERATORS ---
# Calculate loyalty points using augmented assignment
loyalty_points_1234 = 0
loyalty_points_1234 += int(final_payment_1234 // 10000)  # '+=' and '//' floor division operators

# --- 7. IDENTITY OPERATORS ---
# Demonstrating object identity ('is', 'is not') vs value equality ('==')
obj_a_1234 = [1, 2, 3]
obj_b_1234 = [1, 2, 3]
obj_c_1234 = obj_a_1234

same_identity_1234 = (obj_a_1234 is obj_c_1234)      # 'is' operator (True)
diff_identity_1234 = (obj_a_1234 is not obj_b_1234)  # 'is not' operator (True)

# --- 8. BITWISE OPERATORS ---
# Construct Bitmask based on customer metrics:
# Bit 0 (0001 = 1): Member status
# Bit 1 (0010 = 2): Total purchase >= Rp200,000
# Bit 2 (0100 = 4): Item count >= 3
# Bit 3 (1000 = 8): Valid promo code

bit_member_1234 = 1 if is_member_1234 else 0
bit_purchase_1234 = 2 if min_purchase_met_1234 else 0
bit_items_1234 = 4 if min_items_met_1234 else 0
bit_promo_1234 = 8 if valid_promo_1234 else 0

# Bitwise OR (|) to combine into a single status code
status_code_1234 = bit_member_1234 | bit_purchase_1234 | bit_items_1234 | bit_promo_1234

# Bitwise AND (&) to verify individual conditions
check_member_1234 = status_code_1234 & 1
check_promo_1234 = status_code_1234 & 8

# Bitwise XOR (^) to compare against reference baseline (1011 = 11)
reference_code_1234 = 11
xor_result_1234 = status_code_1234 ^ reference_code_1234

# Bitwise Left Shift (<<)
shifted_code_1234 = status_code_1234 << 1

# --- 9. DISPLAY PROGRAM OUTPUT ---
print("\n=== STORE TRANSACTION SYSTEM ===")
print("=== TRANSACTION DATA ===")
print(f"Customer Name: {name_1234}")
print(f"Customer Status: {status_1234}")
print(f"Total Purchase: Rp{total_1234:.0f}")
print(f"Number of Items: {item_count_1234}")
print(f"Promo Code: {promo_code_1234}")

print("\n=== VALIDATION RESULTS ===")
print(f"Purchase >= Rp200000: {min_purchase_met_1234}")
print(f"Number of Items >= 3: {min_items_met_1234}")
print(f"Member Status: {is_member_1234}")
print(f"Promo Code Available: {valid_promo_1234}")
print(f"Gets Discount: {gets_discount_1234}")
print(f"Gets Promo: {gets_promo_1234}")

print("\n=== CALCULATION RESULTS ===")
print(f"Discount: Rp{discount_amount_1234:.0f}")
print(f"Total Payment: Rp{final_payment_1234:.0f}")
print(f"Average Item Price: Rp{avg_item_price_1234:.2f}")
print(f"Loyalty Points Earned: {loyalty_points_1234}")

print("\n=== IDENTITY OPERATOR DEMO ===")
print(f"obj_a == obj_b (Value Check): {obj_a_1234 == obj_b_1234}")
print(f"obj_a is obj_b (Identity Check): {obj_a_1234 is obj_b_1234}")
print(f"obj_a is obj_c (Identity Check): {same_identity_1234}")

print("\n=== BITWISE OPERATIONS ===")
print("=== Transaction Status Code ===")
print(f"Binary Code: {status_code_1234:04b}")
print(f"Decimal Code: {status_code_1234}")

print("\n=== Status Check ===")
print(f"Check Member ({status_code_1234:04b} & 0001): {check_member_1234:04b} (Dec: {check_member_1234})")
print(f"Check Promo  ({status_code_1234:04b} & 1000): {check_promo_1234:04b} (Dec: {check_promo_1234})")

print("\n=== Status Comparison ===")
print(f"Transaction Code: {status_code_1234:04b}")
print(f"Reference Code  : {reference_code_1234:04b}")
print(f"XOR Result ({status_code_1234:04b} ^ {reference_code_1234:04b}): {xor_result_1234:04b} (Dec: {xor_result_1234})")

print("\n=== Shift ===")
print(f"Left Shift ({status_code_1234:04b} << 1): {shifted_code_1234:05b} (Dec: {shifted_code_1234})")
print("\n=== DONE ===")