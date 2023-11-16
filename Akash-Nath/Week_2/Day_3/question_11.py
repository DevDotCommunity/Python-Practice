#Task: Write a program that checks if a string is an anagram of another string. (String Manipulation)

def is_anagram(s1,s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

user_inp1 = input("Enter the first string: ")
user_inp2 = input("Enter the second string: ")

if is_anagram(user_inp1, user_inp2):
    print("The two strings are anagram")
else:
    print("They aren't anagram.")