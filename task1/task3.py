matrix2 = [
    [1, 0, 1],
    [1, 0, 1],
    [1, 1, 1]
]

matrix3 = [
    [0, 0],
    [0, 0]
]
matrix = [
    [1, 0, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [1, 1, 0, 1, 1]
]
dp = [[0 for cols in range(len(matrix[0]))] for rows in range(len(matrix))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
            if min(i, j) == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i-1][j-1]) + 1
print(max(list(map(max, dp))))
