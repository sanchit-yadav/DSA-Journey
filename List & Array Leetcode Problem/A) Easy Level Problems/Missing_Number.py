# Problem: Find the missing number in an n length array that which sequence number is missing till n.

from typing import List
def Find_Missing(num: List[int]):
    n = len(num)
    i = 0
    for i in range(n):
        if i not in num:
            return i
    return n
        
# Example usage
if __name__ == "__main__":
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24,]
    missing_number = Find_Missing(num)
    print(missing_number)