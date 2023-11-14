#!/usr/bin/python3
def rotate_2d_matrix(matrix):
    """
    Given a n*n matrix rotate 90degrees clockwise
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    N = len(matrix)
    for i in range(N//2):
        for j in range(N):
            matrix[j][i], matrix[j][N-1-i] = matrix[j][N-1-i], matrix[j][i]
