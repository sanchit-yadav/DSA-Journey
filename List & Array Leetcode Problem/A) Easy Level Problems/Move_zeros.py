# Problem: Move zeros at the end of the list while maintaining the order of non-zero elements.
# Note that you must do this in-place without making a copy of the array.
def move_zeros(nums):
    # Initialize a pointer for the position of the next non-zero element
    non_zero_index = 0

    # Iterate through the list
    for i in range(len(nums)):
        if nums[i] != 0:
            # If the current element is non-zero, place it at the non_zero_index
            nums[non_zero_index] = nums[i]
            non_zero_index += 1

    # Fill the remaining positions with zeros
    for i in range(non_zero_index, len(nums)):
        nums[i] = 0

    return nums

# Example usage
if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12, 0, 5, 0, 7]
    moved_zeros = move_zeros(nums)
    print(moved_zeros) 