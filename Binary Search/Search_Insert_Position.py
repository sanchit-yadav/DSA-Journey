# Problem : Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

def search_insert_position(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

# Example usage:
if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 5
    print(search_insert_position(nums, target))

    target = 2
    print(search_insert_position(nums, target))

    target = 7
    print(search_insert_position(nums, target))

    target = 0
    print(search_insert_position(nums, target))