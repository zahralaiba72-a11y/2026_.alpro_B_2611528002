first_name = " laiba"
last_name = "shamshad "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())
#problem
#full_name = "Muhammad Rafi Pratama"
#nim = "2610511045"
full_name = "laiba shamshad"
nim = "2611538002"
 
# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().
# Strip extra spaces from the ends
clean_name = full_name.strip()

# Find the index of the space
space_index = clean_name.find(" ")

if space_index == -1:
    # If there is only one word (no space found)
    first_name = clean_name
else:
    # Extract everything before the first space
    first_name = clean_name[:space_index]

# Get the last 3 digits of the NIM
last_3_nim = nim[-3:]

# Combine them in lowercase
username = first_name.lower() + last_3_nim
print(username)