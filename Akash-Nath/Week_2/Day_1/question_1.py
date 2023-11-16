#Task: Write a Python program that finds the length of the longest word in a sentence. (String Manipulation)

def find_longest(sentence):
    words = sentence.split(" ")
    # print(words)
    longest_word_length = 0
    for word in words:
        curr_word_len = len(word)
        if curr_word_len > longest_word_length:
            longest_word_length = curr_word_len
    return longest_word_length
    
long_len = find_longest("I am IronMan")
print(long_len)