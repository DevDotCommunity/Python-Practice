#Task: Write a program that validates an email address. (String Manipulation, Regular Expressions)

user_email = input("Enter your email: ")

if "@" in user_email and ".com" in user_email:
    print("The email is valid")
else:
    print("Enter a valid email.")

# print(user_email)