# Description:
# Given a matrix mat[][] of size M*N.
# Traverse and print the matrix in spiral form.
#
# Approach:
#
#
# Reference:
# https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/
#
# Complexity:
#
from numpy import mat
# O(n)


def traverse_spiral_matrix(mat):
    """Displays an 1D-array after spiral traversing a 2D-array."""

    n=len(mat)
    m=len(mat[0])

    top = 0
    down = n-1
    left = 0
    right = m-1
    direc = 0
    arr = []

    while top <= down and left <= right:
        if direc == 0:
            for i in range(left, right+1):
                arr.append(mat[top][i])
            top = top+1

        elif direc == 1:
            for i in range(top, down+1):
                arr.append(mat[i][right])
            right = right-1

        elif direc==2:
            for i in range(right, left-1, -1):
                arr.append(mat[down][i])
            down = down-1

        elif direc==3:
            for i in range(down, top-1, -1):
                arr.append(mat[i][left])
            left = left+1

        direc = (direc + 1) % 4

    return arr


assert traverse_spiral_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
assert traverse_spiral_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
