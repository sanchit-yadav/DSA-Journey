# Problem: Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

def setZeroes(matrix):
    if not matrix:
        return

    rows, cols = len(matrix), len(matrix[0])
    row_zero = [False] * rows
    col_zero = [False] * cols

    # First pass to find all the rows and columns that need to be zeroed
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_zero[i] = True
                col_zero[j] = True

    # Second pass to set the rows and columns to zero
    for i in range(rows):
        for j in range(cols):
            if row_zero[i] or col_zero[j]:
                matrix[i][j] = 0

# Example usage:
if __name__ == "__main__":
    matrix = [
        [0, 2, 3],
        [4, 8, 6],
        [7, 8, 5]
    ]
    setZeroes(matrix)
    print(matrix)
