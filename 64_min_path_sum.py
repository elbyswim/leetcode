def minPathSum(grid) -> int:
    if len(grid) == 0:
        return 0
    memo = {(0, 0): grid[0][0]}
    k = 1
    while k < len(grid) + len(grid[0]) + 1:
        for i in range(max(0, k - len(grid[0]) + 1), min(k, len(grid) - 1) + 1):
            j = k - i
            memo[(i, j)] = grid[i][j]
            if i == 0:
                memo[(i, j)] += memo[(i, j - 1)]
            elif j == 0:
                memo[(i, j)] += memo[(i - 1, j)]
            else:
                memo[(i, j)] += min(memo[(i, j - 1)], memo[(i - 1, j)])
        k += 1
    return memo[(len(grid) - 1, len(grid[0]) - 1)]


print(minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))


