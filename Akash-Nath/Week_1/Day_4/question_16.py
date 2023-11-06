#Task: Write a Python program to check if a string is a palindrome. (String Manipulation, Loops)

string = input("Enter a string: ")

if string == string[::-1]:
    print(f"The string {string} is palindrome")
else:
    print(f"The string {string} is not palindrome")