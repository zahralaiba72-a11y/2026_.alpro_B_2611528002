number_of_rows = 4
seats_per_row = 5
# Write your code below

seats = [["." for _ in range(seats_per_row)] for _ in range(number_of_rows)]
seats_taken = 0

while True:
    for r in range(number_of_rows):
        print(f"Row {r + 1}: {' '.join(seats[r])}")

    row_num = int(input("Row (0 to stop): "))
    if row_num == 0:
        break

    seat_num = int(input("Seat: "))

    if row_num < 1 or row_num > number_of_rows or seat_num < 1 or seat_num > seats_per_row:
        print("Invalid seat.")
        continue

    r_idx = row_num - 1
    c_idx = seat_num - 1

    if seats[r_idx][c_idx] == "X":
        print("Seat already taken.")
    else:
        seats[r_idx][c_idx] = "X"
        seats_taken += 1
        print("Seat booked.")

print(f"Seats taken: {seats_taken}")