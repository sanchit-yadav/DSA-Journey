# Problem : Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. If target is not found in the array, return [-1, -1].

def search_range(nums, target):
    def find_first(nums, target):
        left, right = 0, len(nums) - 1
        first = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                first = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return first

    def find_last(nums, target):
        left, right = 0, len(nums) - 1
        last = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                last = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return last

    first_index = find_first(nums, target)
    last_index = find_last(nums, target)

    return [first_index, last_index]

# Example usage:
if __name__ == "__main__":
    nums = [5, 7, 7, 7, 7, 8, 8, 10, 10, 10, 10, 12]
    target = 8
    print(search_range(nums, target))

    target = 6
    print(search_range(nums, target))

    target = 10
    print(search_range(nums, target))

    target = 12
    print(search_range(nums, target))


