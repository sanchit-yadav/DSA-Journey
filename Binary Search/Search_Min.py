# Problem : Search the minimum integer in an rotated array.

def search_minimum(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

# Example usage:
if __name__ == "__main__":
    nums = [8, 9, 10, 11, 12, 15, 17, 0, 1, 2, 3, 5]
    print(search_minimum(nums))

    nums = [3, 4, 5, 1, 2]
    print(search_minimum(nums))

    nums = [4, 5, 6, 7, 0, 1, 2]
    print(search_minimum(nums))

    nums = [11, 13, 15, 17]
    print(search_minimum(nums))