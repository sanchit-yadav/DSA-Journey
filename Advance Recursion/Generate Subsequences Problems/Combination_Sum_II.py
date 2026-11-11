# Problem : Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.Each number in candidates may only be used once in the combination.

#Note: The solution set must not contain duplicate combinations.

def combination_sum_ii(candidates, target):
    def backtrack(start, path, target):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            # Skip duplicates
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            backtrack(i + 1, path + [candidates[i]], target - candidates[i])

    candidates.sort()  # Sort to handle duplicates
    result = []
    backtrack(0, [], target)
    return result

# Example usage:
if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5, 2]
    target = 12
    print(combination_sum_ii(candidates, target))