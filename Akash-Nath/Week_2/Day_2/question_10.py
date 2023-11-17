#Task: Write a program to determine if a given string is a valid palindrome considering only alphanumeric characters and ignoring cases. (String Manipulation)

def is_palindrome(string):
    cleaned_str = ""
    for char in string:
        if char.isalnum():
            cleaned_str += char.lower()
            
    reversed_string = string[::-1]
    
    return cleaned_str == reversed_string

user_inp = input("Enter the string: ")

if is_palindrome(user_inp):
    print(f"Your string '{user_inp}' is palindrome")
else:
    print("It's not palindrome")