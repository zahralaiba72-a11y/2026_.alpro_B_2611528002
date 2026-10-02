# Program Framed Palindromic Crystal Hourglass (Week 5)
# File Name: tugas5_8002.py
# All variables end with the last 4 digits of the student ID (NIM)

print("=== FRAMED PALINDROMIC CRYSTAL HOURGLASS PROGRAM (WEEK 5) ===")
n_8002 = int(input("Enter hourglass scale size (N): "))

# 1. TOP HORIZONTAL BORDER
# Format: # + '=' repeated (4 * N + 5) times + #
print("#", end="")
for border_8002 in range(4 * n_8002 + 5):
    print("=", end="")
print("#")

# 2. PHASE 1: UPPER HOURGLASS (Row N down to 1)
for row_8002 in range(n_8002, 0, -1):
    print("| ", end="")  # Left vertical border + 1 padding space
    
    # Left balancing spaces: 2 * (N - row)
    for spasi_8002 in range(2 * (n_8002 - row_8002)):
        print(" ", end="")
        
    # Descending number sequence: row down to 1
    for num_8002 in range(row_8002, 0, -1):
        print(num_8002, end=" ")
        
    # Center crystal axis
    print("<*>", end="")
    
    # Ascending number sequence: 1 up to row
    for num_8002 in range(1, row_8002 + 1):
        print(f" {num_8002}", end="")
        
    # Right balancing spaces: 2 * (N - row)
    for spasi_8002 in range(2 * (n_8002 - row_8002)):
        print(" ", end="")
        
    print(" |")  # Right padding space + vertical border

# 3. PHASE 2: HOURGLASS CENTER AXIS (Singularity)
print("|", end="")
# Left balancing spaces: (2 * N + 1)
for spasi_8002 in range(2 * n_8002 + 1):
    print(" ", end="")

# Center crystal axis
print("<*>", end="")

# Right balancing spaces: (2 * N + 1)
for spasi_8002 in range(2 * n_8002 + 1):
    print(" ", end="")
print("|")

# 4. PHASE 3: LOWER HOURGLASS (Row 1 up to N)
for row_8002 in range(1, n_8002 + 1):
    print("| ", end="")  # Left vertical border + 1 padding space
    
    # Left balancing spaces: 2 * (N - row)
    for spasi_8002 in range(2 * (n_8002 - row_8002)):
        print(" ", end="")
        
    # Descending number sequence: row down to 1
    for num_8002 in range(row_8002, 0, -1):
        print(num_8002, end=" ")
        
    # Center crystal axis
    print("<*>", end="")
    
    # Ascending number sequence: 1 up to row
    for num_8002 in range(1, row_8002 + 1):
        print(f" {num_8002}", end="")
        
    # Right balancing spaces: 2 * (N - row)
    for spasi_8002 in range(2 * (n_8002 - row_8002)):
        print(" ", end="")
        
    print(" |")  # Right padding space + vertical border

# 5. BOTTOM HORIZONTAL BORDER
print("#", end="")
for border_8002 in range(4 * n_8002 + 5):
    print("=", end="")
print("#")