# Problem: Find the most consecutive number of ones in an array.

from typing import List
def Consecutive_One(nums: List[int]):
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

# Example usage
if __name__ == "__main__":
    nums = [1, 1, 0, 1, 1, 1]
    max_consecutive_ones = Consecutive_One(nums)
    print(max_consecutive_ones)


