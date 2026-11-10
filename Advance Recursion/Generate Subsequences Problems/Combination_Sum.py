# Problem : Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order. The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

def combination_sum(candidates, target):
    def backtrack(start, path, target):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            backtrack(i, path + [candidates[i]], target - candidates[i])

    result = []
    backtrack(0, [], target)
    return result

# Example usage:
if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 8
    print(combination_sum(candidates, target))