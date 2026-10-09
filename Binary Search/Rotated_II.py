# Problem: Given an integer array nums sorted in ascending order (with duplicates) and an integer target, write a function to search target in nums. If target exists, then return true. Otherwise, return false.

def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
            continue
        if nums[mid] <= nums[right]:
            if nums[mid]<=target<=nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[left]<=target<=nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

    return False

# Example usage:
if __name__ == "__main__":
    arr = [5, 5, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 0, 1, 2, 3, 4, 4, 4, 4]
    print(search(arr, 4))