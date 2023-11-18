sentence = input(' enter a sentence ')
word_occurrences = {}
word = ""
for char in sentence:
    if char.isalnum() or char == "'":
        word += char
    elif word:
        word_occurrences[word.lower()] = word_occurrences.get(word.lower(), 0) + 1
        word = ""
if word:
    word_occurrences[word.lower()] = word_occurrences.get(word.lower(), 0) + 1
for word, count in word_occurrences.items():
    print(f"{word}: {count}")
