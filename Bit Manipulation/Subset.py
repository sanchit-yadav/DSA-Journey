# Problem : Given an integer array nums of unique elements, return all possible subsets (the power set).

def subsets(nums):
    # Initialize the result list with an empty subset
    result = [[]]
    
    # Iterate through each number in the input array
    for num in nums:
        # For each existing subset, create a new subset that includes the current number
        new_subsets = [curr + [num] for curr in result]
        # Add the new subsets to the result list
        result.extend(new_subsets)
    
    return result

# Example usage:
nums = [1, 2, 3]
result = subsets(nums)
print(f"All possible subsets of {nums} are: {result}")