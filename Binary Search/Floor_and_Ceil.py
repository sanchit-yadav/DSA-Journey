# Problem : You're given a sorted array 'a' of 'n' integers and an integer 'x' Find the floor and ceiling of 'x' in 'a[0..n-1]'.

from typing import List

def FloorCeil(nums : List, target: int):
    left, right = 0, len(nums) - 1
    floor, ceil = -1, -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return (nums[mid], nums[mid])
        elif nums[mid] < target:
            floor = nums[mid]
            left = mid + 1
        else:
            ceil = nums[mid]
            right = mid - 1

    return (floor, ceil)

# Example usage:
if __name__ == "__main__":
    nums = [1, 2, 8, 10, 10, 12, 19]
    target = 5
    print(FloorCeil(nums, target))

    target = 20
    print(FloorCeil(nums, target))

    target = 0
    print(FloorCeil(nums, target))