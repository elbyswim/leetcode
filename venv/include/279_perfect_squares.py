def numSquares(n):
    memo = [0] * (n + 1)
    queue = [0]
    while True:
        i = queue.pop(0)
        square = 1
        j = i + square ** 2
        while j <= n:
            if memo[j] <= 0:
                memo[j] = 1 + memo[i]
                queue.append(j)
            if j == n:
                return memo[j]
            square += 1
            j = i + square ** 2


print(numSquares(12))
