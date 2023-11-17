#Task: Write a Python program to find the first non-repeating character in a string. (String Manipulation)

def first_non_repeating_char(input_string):
    char_count = {}

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    for char in input_string:
        if char_count[char] == 1:
            return char

    return None

input_str = "aabbccddeeffg"
result = first_non_repeating_char(input_str)

if result:
    print(f"The first non-repeating character is: {result}")
else:
    print("No non-repeating character found.")
