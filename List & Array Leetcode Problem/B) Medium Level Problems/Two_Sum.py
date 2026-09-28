# Problem: You are given an array of integers and an integer target, return indices of the two numbers such that they add up to target.

from typing import List
def Two_sum(arr: List[int], target: int):
    n = len(arr)
    hash_map = {}
    for i in range(n):
        remaining = target - arr[i]
        if remaining in hash_map:
            return [hash_map[remaining], i]
        hash_map[arr[i]] = i

# Example usage
if __name__ == "__main__":
    arr = [2, 7, 11, 1, 15]
    target = 12
    result = Two_sum(arr, target)
    print(result)  # Output: [0, 1]
