# Problem: You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.You should return the array of nums such that Every consecutive pair of integers have opposite signs, For all integers with the same sign, the order in which they were present in nums is preserved, rearranged array begins with a positive integer.


from typing import List
def rearrange_by_sign(nums: List[int]) -> List[int]:
    positive_nums = [num for num in nums if num > 0]
    negative_nums = [num for num in nums if num < 0]

    rearranged_array = []
    for pos, neg in zip(positive_nums, negative_nums):
        rearranged_array.append(pos)
        rearranged_array.append(neg)

    return rearranged_array

# Example usage
if __name__ == "__main__":
    nums = [3, 1, -2, -5, 2, -4]
    result = rearrange_by_sign(nums)
    print(result)
