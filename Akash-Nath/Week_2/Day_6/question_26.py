#Task: Write a Python program to reverse the words in a sentence. (String Manipulation)

def reverse_words(sentence):
    words = sentence.split(" ")
    reverse_sentence = " ".join(reversed(words))
    return reverse_sentence

# if __name__ == "__main__":
sentence = input("Enter the sentence: ")
print(reverse_words(sentence))