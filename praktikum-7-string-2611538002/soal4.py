# Masking  a phone  number
phone = "081234567890"
masked = phone[:4] + "*" * 4 + phone[-4:]
print(masked)
#for 0812*****890
phone = "081234567890"
masked = phone[:4] + "*" * 5 + phone[-3:]
print(masked)
#for 0812****789
phone = "08123456789"
masked = phone[:4] + "*" * 4 + phone[-3:]
print(masked)

# for 08 + your NIM/0826**002
phone = "082611538002"
masked = phone[:4] + "*" * 2 + phone[-3:]
print(masked)