#Task: Write a program to check if a given string is a pangram (contains every letter of the alphabet at least once). (String Manipulation)

import string

def check_pangram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in string.lower():
            return False
    return True

print(check_pangram("The quick brown fox jumps over the lazy dog"))