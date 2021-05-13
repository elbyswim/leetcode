class Solution:
    def calculateMinimumHP(self, dungeon):
        for i in range(len(dungeon)):
            for j in range(len(dungeon[0])):
                if i == j == 0:
                    memo = [(dungeon[i][j], dungeon[i][j], dungeon[i][j], dungeon[i][j])]
                elif i == 0:
                    current = memo[j - 1][1] + dungeon[i][j]
                    lowest = min(memo[j - 1][0], current)
                    memo.append((lowest, current, lowest, current))
                elif j == 0:
                    current = memo[j][1] + dungeon[i][j]
                    lowest = min(memo[j][0], current)
                    memo[j] = (lowest, current, lowest, current)
                else:
                    currentright1 = memo[j - 1][1] + dungeon[i][j]
                    currentdown1 = memo[j][1] + dungeon[i][j]
                    rightmin = min(memo[j - 1][0], currentright1)
                    downmin = min(memo[j][0], currentdown1)
                    if rightmin > downmin:
                        min1, current1 = rightmin, currentright1
                    else:
                        min1, current1 = downmin, currentdown1
                    currentright2 = memo[j - 1][3] + dungeon[i][j]
                    currentdown2 = memo[j][3] + dungeon[i][j]
                    if currentright2 > currentdown2:
                        min2, current2 = min(memo[j - 1][2], currentright2), currentright2
                    elif currentright2 < currentdown2:
                        min2, current2 = min(memo[j][2], currentdown2), currentdown2
                    else:
                        min2, current2 = min(max(memo[j][2], memo[j - 1][2]), currentdown2), currentdown2
                    memo[j] = (min1, current1, min2, current2)
        return max(1, 1 - max(memo[-1][0], memo[-1][2]))


soln = Solution()
tests = [
    # [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]],
    [[1, -3, 3], [0, -2, 0], [-3, -3, -3]]
]
for test in tests:
    print(soln.calculateMinimumHP(test))
