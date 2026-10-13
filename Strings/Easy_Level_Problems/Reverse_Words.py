# Problem: Reverse the order of words in a given string.

def reverse_words(s):
    words = s.split()
    words.reverse()
    result = " ".join(words)
    return result


#Example Usage
if __name__== "__main__":
    str1 = "The sky is Blue"
    str2 = "What is the colour of your shirt ?"
    print(reverse_words(str1))
    print(reverse_words(str2))