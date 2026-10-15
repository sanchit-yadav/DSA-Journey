# Problem: Given two strings s and t, return true if t is an anagram of s, and false otherwise. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    count_s = {}
    count_t = {}
    
    for char in s:
        count_s[char] = count_s.get(char, 0) + 1
    
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1
    
    return count_s == count_t

# Example usage:
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))
    
    s = "rat"
    t = "car"
    print(isAnagram(s, t))