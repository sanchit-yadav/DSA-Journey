# Problem : Two strings s and t are isomorphic if the characters in s can be replaced to get t. All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    
    mapping_s_to_t = {}
    mapping_t_to_s = {}
    
    for char_s, char_t in zip(s, t):
        # Check if there is a mapping for char_s
        if char_s in mapping_s_to_t:
            # If the mapped character does not match char_t, return False
            if mapping_s_to_t[char_s] != char_t:
                return False
        else:
            # Create a new mapping from char_s to char_t
            mapping_s_to_t[char_s] = char_t
        
        # Check if there is a mapping for char_t
        if char_t in mapping_t_to_s:
            # If the mapped character does not match char_s, return False
            if mapping_t_to_s[char_t] != char_s:
                return False
        else:
            # Create a new mapping from char_t to char_s
            mapping_t_to_s[char_t] = char_s
    
    return True

# Example usage:
if __name__ == "__main__":
    s = "egg"
    t = "add"
    print(isIsomorphic(s, t))
    
    s = "foo"
    t = "bar"
    print(isIsomorphic(s, t))
    
    s = "paper"
    t = "title"
    print(isIsomorphic(s, t))
    
    s = "ab"
    t = "aa"
    print(isIsomorphic(s, t))