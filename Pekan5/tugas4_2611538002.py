# === ALPRO ADVENTURE PARK TICKET COUNTER SYSTEM ===
print("=== ALPRO ADVENTURE PARK TICKET COUNTER SYSTEM ===")

# 1. Visitor Data Input
nama_1001 = input("Enter Visitor Name              : ")
umur_1001 = int(input("Enter your age                  : "))
sim_1001 = input("Do you already have a SIM C (y/t): ").strip().lower()[0]

# Display Menu Options
print("Attraction Package Choices (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

paket_1001 = int(input("Enter package number (1-5)       : "))
jumlah_tiket_1001 = int(input("Enter number of tickets           : "))

# Single IF validation for ticket quota
if jumlah_tiket_1001 <= 0:
    print("Warning: Ticket quota is invalid!")

# 2. Match-Case for Attraction Selection
match paket_1001:
    case 1:
        nama_paket_1001 = "Wahana Safari Rimba"
        harga_satuan_1001 = 50000
    case 2:
        nama_paket_1001 = "Wahana Arung Jeram"
        harga_satuan_1001 = 75000
    case 3:
        nama_paket_1001 = "Wahana Motor ATV Ekstrim"
        harga_satuan_1001 = 120000
    case 4:
        nama_paket_1001 = "Wahana Roller Coaster Kilat"
        harga_satuan_1001 = 100000
    case 5:
        nama_paket_1001 = "Wahana All-Access VIP"
        harga_satuan_1001 = 220000
    case _:
        print("Invalid attraction package!")
        exit()  # Stops execution if invalid choice

# Input Member and Promo voucher status
is_member_1001 = input("Are you a member? (y/t)           : ").strip().lower()
kode_promo_valid_1001 = input("Is the promo code valid? (y/t)    : ").strip().lower()

print("\n--- RIDER ELIGIBILITY ---")

# 3. Control Permission Validation using if-elif-else & logical operators
if paket_1001 == 3:
    if umur_1001 >= 17 and sim_1001 == 'y':
        print("Access Status: You are an adult and may ride the ATV by yourself.")
    elif umur_1001 >= 17 and sim_1001 != 'y':
        print("Access Status: You are an adult but may not operate the ATV (must be accompanied by an instructor).")
    elif umur_1001 < 17 and sim_1001 == 'y':
        print("Access Status: Invalid identity: Not old enough to have a driving license.")
    else:
        print("Access Status: You are underage and may not operate the ATV.")
else:
    if umur_1001 >= 10:
        print("Access Status: You meet the age eligibility requirement for this attraction.")
    else:
        print("Access Status: You do not meet the minimum age requirement for this attraction.")

# 4. Multi-IF for Tiered Cumulative Discounts
subtotal_1001 = harga_satuan_1001 * jumlah_tiket_1001
total_diskon_persen_1001 = 0

if subtotal_1001 >= 200000:
    total_diskon_persen_1001 += 10

if is_member_1001 in ['y', 'ya']:
    total_diskon_persen_1001 += 5

if kode_promo_valid_1001 in ['y', 'ya']:
    total_diskon_persen_1001 += 15

if jumlah_tiket_1001 >= 5:
    total_diskon_persen_1001 += 5

# Calculations
nominal_diskon_1001 = subtotal_1001 * (total_diskon_persen_1001 / 100)
total_bayar_1001 = subtotal_1001 - nominal_diskon_1001

# 5. Output Payment Details & Audit
print("\n--- Payment Details ---")
print(f"Purchase Subtotal : Rp {subtotal_1001:,.0f}")
print(f"Total Discount    : {total_diskon_persen_1001}% (Rp {nominal_diskon_1001:,.0f})")
print(f"Total Payment     : Rp {total_bayar_1001:,.0f}")

if total_bayar_1001 > 300000:
    print("Service Note      : Congratulations! You are entitled to a Free Souvenir.")
else:
    print("Service Note      : Thank you for visiting.")

print("Program Completed")