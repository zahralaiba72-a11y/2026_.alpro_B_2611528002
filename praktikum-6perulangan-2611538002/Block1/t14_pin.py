#code order;K, H, B, E, C, I, G, E, J, D, F, A
correct_pin ="1234"
MAX_ATTEMPTS = 3
attempts = 1
pin = input("Enter your PIN: ")

while pin != correct_pin and attempts < MAX_ATTEMPTS:
    print("Incorrect PIN. Please try again.")
    attempts += 1
    pin = input("Enter your PIN: ")
    
if pin == correct_pin:
    print("PIN accepted. Access granted.")
else:
    print("Too many incorrect attempts. Account locked.")
