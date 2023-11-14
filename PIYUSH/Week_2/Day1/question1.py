
input_sentence = input("Enter a sentence: ")
words = input_sentence.split()
word_lengths = map(len, words)
longest_word_length = max(word_lengths)
print(f"The length of the longest word in the sentence is: {longest_word_length}")
