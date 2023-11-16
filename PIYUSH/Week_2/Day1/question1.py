sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Find the length of the longest word
max_length = 0
for word in words:
    current_length = len(word)
    if current_length > max_length:
        max_length = current_length

print("Length of the longest word:", max_length)
