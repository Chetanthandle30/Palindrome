# To check if a word is palindrome
name1 = (input("Enter a word to check if it is a palindrome"))
name2 = ""
for i in name1:
    name2 = i + name2
if name1 == name2:
    print(name1, "is a palindrome")
else:
    print(name1, "is not a palindrome")
