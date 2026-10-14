# Problem : Find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string.

def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Start with the first string as the prefix
    prefix = strs[0]
    
    for string in strs[1:]:
        # Update the prefix by comparing it with each string
        while not string.startswith(prefix):
            # Shorten the prefix by removing the last character
            prefix = prefix[:-1]
            # If the prefix becomes empty, return an empty string
            if not prefix:
                return ""
    
    return prefix

# Example usage:
if __name__ == "__main__":
    strings = ["flower", "flow", "flight"]
    print(longestCommonPrefix(strings))
    
    strings = ["dog", "racecar", "car"]
    print(longestCommonPrefix(strings))
    
    strings = ["interspecies", "interstellar", "interstate"]
    print(longestCommonPrefix(strings))
    
    strings = ["throne", "throne"]
    print(longestCommonPrefix(strings))
    
    strings = ["throne", "dungeon"]
    print(longestCommonPrefix(strings))