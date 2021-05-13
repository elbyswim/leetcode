class Solution:
    def islandPerimeter(self, grid) -> int:
        stack = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    stack.append((i, j))
                    break
            if len(stack):
                break
        seen = set()
        p = 0
        while len(stack):
            i, j = stack.pop()
            if (i, j) in seen:
                continue
            seen.add((i, j))
            if i > 0 and grid[i - 1][j]:
                stack.append((i - 1, j))
            else:
                p += 1
            if i < len(grid) - 1 and grid[i + 1][j]:
                stack.append((i + 1, j))
            else:
                p += 1
            if j > 0 and grid[i][j - 1]:
                stack.append((i, j - 1))
            else:
                p += 1
            if j < len(grid[0]) - 1 and grid[i][j + 1]:
                stack.append((i, j + 1))
            else:
                p += 1
        return p

soln = Solution()
soln.islandPerimeter([[0],[1]])