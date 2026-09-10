nums = [5, 2, 3, 5, 2, 1, 4, 3, 5]

hash_map = {}
n = len(nums)

for i in range(0, n):
    hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1