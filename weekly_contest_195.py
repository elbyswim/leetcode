class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        visited = {(x, y)}
        for d in path:
            if d == 'N':
                y += 1
            elif d == 'S':
                y -= 1
            elif d == 'E':
                x += 1
            elif d == 'W':
                x -= 1
            if (x, y) in visited:
                return True
            else:
                visited.add((x, y))
        return False

soln = Solution()
print(soln.isPathCrossing('NS'))