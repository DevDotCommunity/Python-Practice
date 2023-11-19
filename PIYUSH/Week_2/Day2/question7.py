
input_string = input("Enter a string: ")
non_char = next((char for char in input_string if input_string.count(char) == 1), None)
print(f"The first non-repeating character is: {non_char}")
