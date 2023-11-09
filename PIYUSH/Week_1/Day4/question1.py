
def isPalindrome(str): 
    if (str == str[::-1]) : 
        return "The string is a palindrome." 
    else: 
        return "The string is not a palindrome." 

str = input ("Enter string: ") 
 
print(isPalindrome(str))
