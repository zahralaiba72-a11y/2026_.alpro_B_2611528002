# Store data (replace with your own name and NIM)
name = "Laiba shamshad"
nim = "2611538002"

# username from Question 6 logic
clean_name = name.strip()
space_index = clean_name.find(" ")

if space_index == -1:
    first_name = clean_name
else:
    first_name = clean_name[:space_index]

username = first_name.lower() + nim[-3:]

# Extract intake year from NIM using slicing
intake = "20" + nim[:2]

# Print the 30-character wide Student Card
print("-" * 30)
print("STUDENT CARD".center(30))
print("-" * 30)
print("Name".ljust(10) + ": " + name.title())
print("NIM".ljust(10) + ": " + nim)
print("Username".ljust(10) + ": " + username)
print("Intake".ljust(10) + ": " + intake)
print("-" * 30)