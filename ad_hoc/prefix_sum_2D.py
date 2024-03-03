# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/description/
def compute_prefix_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    prefix_sum = [[0] * cols for _ in range(rows)]
    prefix_sum[0][0] = matrix[0][0]
    for i in range(1, rows):
        prefix_sum[i][0] = prefix_sum[i - 1][0] + matrix[i][0]
    for j in range(1, cols):
        prefix_sum[0][j] = prefix_sum[0][j - 1] + matrix[0][j]

    for i in range(1, rows):
        for j in range(1, cols):
            prefix_sum[i][j] = (prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + matrix[i][j])

    return prefix_sum
