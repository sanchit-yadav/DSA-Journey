# Problem : Given two integers start and goal, return the minimum number of bit flips to convert start to goal.

def minBitFlips(start, goal):
    # XOR the two numbers to find the differing bits
    xor_result = start ^ goal
    
    # Count the number of set bits (1s) in the XOR result
    count = 0
    while xor_result:
        count += xor_result & 1  # Increment count if the least significant bit is 1
        xor_result >>= 1         # Right shift to check the next bit
    
    return count

# Example usage:
start = 10
goal = 7
result = minBitFlips(start, goal)
print(f"Minimum number of bit flips to convert {start} to {goal} is: {result}")