# Problem: Search an element from an array and give the position of that element if element is not in that array return -1.
from typing import List
def Linear_search(arr: List[int], x: int):
    for idx in range(len(arr)):
        if arr[idx] == x:
            return idx+1
    return -1

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 10, -12, 0, 7, -18]
    x = 10
    position = Linear_search(arr, x)
    print(position)