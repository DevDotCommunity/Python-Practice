
str = input("Enter the first string: ")
str2 = input("Enter the second string: ")
is_anagram = sorted(str.lower()) == sorted(str2.lower())
print(f"The strings are {'anagrams' if is_anagram else 'not anagrams'}.")
