#Task: Write a program to count the number of words in a sentence. (String Manipulation, Loops)

sentence = input("Enter a sentence: ")

words = sentence.split(" ")

print(f"There are {len(words)} in the sentence")