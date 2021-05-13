def oddCells(n, m, indices):
    matrix = [[0] * m] * n
    count = 0
    for pair in indices:
        for cell in matrix[pair[0]]:
            cell += 1
        for row in range(n):
            matrix[row][pair[1]] += 1
    for row in range(n):
        for col in range(m):
            if not matrix[row][col] % 2:
                count += 1
    return count

print(oddCells(2, 3, [[0, 1], [1, 1]]))
print(oddCells(2, 2, [[0, 0], [1, 1]]))
