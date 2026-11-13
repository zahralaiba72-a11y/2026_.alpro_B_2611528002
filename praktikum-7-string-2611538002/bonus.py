# Test sentence
sentence = "malam"

# 1. Convert to lowercase and remove all spaces
clean_sentence = sentence.lower().replace(" ", "")

# 2. Reverse the cleaned sentence
reversed_sentence = clean_sentence[::-1]

# 3. Check if it's a palindrome and display the result
if clean_sentence == reversed_sentence:
    print("Palindrome")
else:
    print("Not a palindrome")