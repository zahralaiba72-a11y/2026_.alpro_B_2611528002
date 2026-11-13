text = "Informatika"
print(text[10])
print (text.upper())
print (text[0:20])
#partB
text = "Algoritma dan Pemrograman"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)
#replace text with your name
text = "Laiba Shamshad"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)
