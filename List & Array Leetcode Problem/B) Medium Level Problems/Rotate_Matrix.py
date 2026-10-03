# Problem : Rotate a given n x n 2D matrix representing an image by 90 degrees (clockwise).

from typing import List

def rotate_matrix(Matrix: List[int]):
    n = len(Matrix)
    for i in range(n-1):
        for j in range(i+1, n):
            Matrix[i][j], Matrix[j][i] = Matrix[j][i], Matrix[i][j]
    for row in Matrix:
        row.reverse()

# Example usage:
if __name__ == "__main__":
    Matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate_matrix(Matrix)
    print(Matrix)
    