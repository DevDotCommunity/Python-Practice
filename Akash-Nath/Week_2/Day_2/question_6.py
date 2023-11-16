#Task: Write a program that checks if a string is an anagram of another string. (String Manipulation)

def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1)==sorted(str2)

str1 = input("Enter the first word: ")
str2 = input("Enter the second word: ")

if is_anagram(str1, str2):
    print("They are anagram.")
    
else:
    print("They are not anagram.")