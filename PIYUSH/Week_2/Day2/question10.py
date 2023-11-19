
  input_string = " ENTER A SENTENCE "
cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
is_palindrome = cleaned_string == cleaned_string[::-1]
if is_palindrome:
    print(f'The string "{input_string}" is a valid palindrome.')
else:
    print(f'The string "{input_string}" is not a valid palindrome.')
