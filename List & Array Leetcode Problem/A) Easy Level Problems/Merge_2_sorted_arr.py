# Problem : Merge two sorted array such that there is only unique elements  in merge array.

from typing import List
def Merge_array(a: List[int], b: List[int]):
    i, j = 0, 0
    result = []
    n, m = len(a), len(b)

    while i < n and j < m:
        # Skip duplicates in a[]
        while i > 0 and i < n and a[i] == a[i-1]:
            i += 1
        # Skip duplicates in b[]
        while j > 0 and j < m and b[j] == b[j-1]:
            j += 1
        if i >= n or j >= m:
            break

        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        elif a[i] > b[j]:
            result.append(b[j])
            j += 1
        else:  # equal elements
            result.append(a[i])
            i += 1
            j += 1

    # Add remaining elements of a[]
    while i < n:
        if i == 0 or a[i] != a[i-1]:
            result.append(a[i])
        i += 1

    # Add remaining elements of b[]
    while j < m:
        if j == 0 or b[j] != b[j-1]:
            result.append(b[j])
        j += 1

    return result

# Example usage
if __name__ == "__main__":
    a = [1, 2, 2, 3, 4, 5]
    b = [2, 3, 5, 6, 7]
    merged_array = Merge_array(a, b)
    print(merged_array)  