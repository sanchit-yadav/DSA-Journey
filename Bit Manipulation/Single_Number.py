# Problem : Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

def singleNumber(nums):
    # Initialize a variable to hold the result
    result = 0
    
    # XOR all the numbers in the array
    for num in nums:
        result ^= num  # XOR operation will cancel out the numbers appearing twice
    
    return result

# Example usage:
nums = [4, 1, 2, 1, 2]
result = singleNumber(nums)
print(f"The single number in the array {nums} is: {result}")