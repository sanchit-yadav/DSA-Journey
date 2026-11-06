# Problem : Given an integer n, the task is to generate all binary strings of size n without consecutive 1's.

def generate_binary_strings(n):
    # Initialize the result list to store valid binary strings
    result = []
    
    # Helper function to generate binary strings recursively
    def backtrack(current_string, last_char):
        # If the current string has reached the desired length, add it to the result
        if len(current_string) == n:
            result.append(current_string)
            return
        
        # Add '0' to the current string and continue recursion
        backtrack(current_string + '0', '0')
        
        # Add '1' to the current string only if the last character was not '1'
        if last_char != '1':
            backtrack(current_string + '1', '1')
    
    # Start the recursion with an empty string and no last character
    backtrack('', '')
    
    return result

# Example usage:
if __name__ == "__main__":
    n = 3
    result = generate_binary_strings(n)
    print(f"All binary strings of size {n} without consecutive 1's are: {result}")
