# problem : Given an array arr of integers, return the sums of all subsets in the list.  Return the sums in any order.

def subset_sums(arr):
    def backtrack(start, current_sum):
        if start == len(arr):
            result.append(current_sum)
            return
        # Include the current element
        backtrack(start + 1, current_sum + arr[start])
        # Exclude the current element
        backtrack(start + 1, current_sum)

    result = []
    backtrack(0, 0)
    return result

# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3]
    print(subset_sums(arr))