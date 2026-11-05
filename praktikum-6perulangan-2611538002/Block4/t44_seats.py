blocked_seat = 3  # You can change this value to test

for row in range(1, 4):
    print("Row", row, end=": ")
    for seat in range(1, 6):
        if seat == blocked_seat:
            break
        print(seat, end=" ")
    print()  # Moves to the next line after each row