# Problem : Keep all unique elements in same array at starting then include elements already in array. After removing duplicates, return the number of unique elements.
def removeDuplicates(self, nums: list[int]) -> int:
    n = len(nums)
    if n==1:
        return 1
    i = 0
    j = i+1
    while j<n:
        if nums[j] != nums[i]:
            i += 1
            nums[i],nums[j]=nums[j],nums[i]
        j += 1
    return i+1

# Example usage:
if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 8, 9, 9, 10]
    result = removeDuplicates(None, nums)
    print(f"Number of unique elements: {result}")
    print(f"Array after removing duplicates: {nums[:result]}")