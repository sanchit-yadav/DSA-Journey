# Problem : Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

def frequencySort(s):
    # Create a dictionary to count the frequency of each character
    freq_dict = {}
    for char in s:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    
    # Sort the characters based on frequency and then by character
    sorted_chars = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
    
    # Build the result string based on sorted characters and their frequencies
    result = ''.join(char * freq for char, freq in sorted_chars)
    
    return result

# Example usage:
if __name__ == "__main__":
    s = "aabcddeff"
    print(frequencySort(s))
    s = "tree"
    print(frequencySort(s))
    s = "cccaaa"
    print(frequencySort(s))