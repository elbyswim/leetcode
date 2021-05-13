class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        checked = set()

        def dfs(i, j):
            nonlocal checked
            if any([i < 0, j < 0, i > len(board) - 1, j > len(board[0]) - 1, (i, j) in checked]):
                return
            if board[i][j] == 'O':
                checked.add((i, j))
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)

        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0]) - 1)
        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board) - 1, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in checked:
                    board[i][j] = 'X'


soln = Solution()
tests = [
    [['X', 'X', 'X'], ['X', 'O', 'X'], ['X', 'X', 'X']],
    [['O', 'X', 'O'], ['X', 'O', 'X'], ['O', 'X', 'O']],
    [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
]
for test in tests:
    soln.solve(test)
print(tests)
