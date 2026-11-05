total = 0

while True:
    number = int(input("Enter a number: "))
    
    if number < 0:
        break  # A negative number stops the loop
    elif number == 0:
        continue  # The number 0 is skipped
    else:
        print(f"Positive number: {number}")
        total += number  # Added to total

print(f"Total: {total}")