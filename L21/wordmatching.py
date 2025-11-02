#Write a Python program to count the number of strings where the string length is two or more, and the first and last characters are the same from a given list of strings.
# function to check whether
# first and last character of words match
def match_word(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1 
            lst.append(word)
    print("List of words with first and last character same\n", lst) 
    return ctr

count = match_word(['abc', 'cfc', 'xyz' , 'aba', '1221'])
print("Number of words having first and last character same:", count)
