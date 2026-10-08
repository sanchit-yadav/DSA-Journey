# Problem : Given a sorted array of integers and a target value, return the number of occurrences of the target in the array.

from typing import List

def count_occurrences(nums: List, target: int):
    left, right = 0, len(nums) - 1
    count = 0

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            count += 1
            # Check for occurrences on the left side
            l, r = mid - 1, mid + 1
            while l >= 0 and nums[l] == target:
                count += 1
                l -= 1
            while r < len(nums) and nums[r] == target:
                count += 1
                r += 1
            break
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return count

# Example usage:
if __name__ == "__main__":
    nums = [1, 2, 2, 2, 3, 4, 5]
    target = 2
    print(count_occurrences(nums, target))

    target = 6
    print(count_occurrences(nums, target))

    target = 1
    print(count_occurrences(nums, target))

    target = 5
    print(count_occurrences(nums, target))