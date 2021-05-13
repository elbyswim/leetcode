def isValidSudoku(board):
    seen = {}
    for i in range(1, 10):
        seen[str(i)] = [set(), set(), set()]
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                group = i // 3 * 3 + j // 3
                if i in seen[board[i][j]][0] or j in seen[board[i][j]][1] or group in seen[board[i][j]][2]:
                    return False
                seen[board[i][j]][0].add(i)
                seen[board[i][j]][1].add(j)
                seen[board[i][j]][2].add(group)
    return True


test = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku(test))
