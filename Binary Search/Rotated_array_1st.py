# Problem : There is an integer array(With unique elements) nums sorted in ascending order is possibly left rotated at an unknown index and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
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

    return -1

# Example usage:
if __name__ == "__main__":
    nums = [8, 9, 10, 11, 12, 15, 17, 0, 1, 2, 3, 5]
    target = 8
    print(search(nums, target))

    target = 6
    print(search(nums, target))

    target = 3
    print(search(nums, target))

    target = 12
    print(search(nums, target))