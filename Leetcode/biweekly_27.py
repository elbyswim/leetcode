class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites, queries):
        inNeighbours = {i: set() for i in range(n)}
        for prereq in prerequisites:
            inNeighbours[prereq[1]].add(prereq[0])
        prereqs = set(tuple(prereq) for prereq in prerequisites)
        len1, len2 = 0, len(prereqs)
        while len1 != len2:
            len1 = len(prereqs)
            for prereq in prerequisites:
                new = inNeighbours[prereq[1]].union(inNeighbours[prereq[0]]).difference(inNeighbours[prereq[1]])
                for i in new:
                    prereqs.add((i, prereq[1]))
                inNeighbours[prereq[1]] = inNeighbours[prereq[1]].union(new)
            len2 = len(prereqs)
        ans = []
        for query in queries:
            ans.append(tuple(query) in prereqs)
        return ans

    def cherryPickup(self, grid):
        i, j = 0, len(grid[0]) - 1
        row = 0
        memo = {(i, j): grid[row][i] + grid[row][j]}
        row = 1
        while row < len(grid):
            new = {}
            for pos in memo:
                for new_i in range(max(0, pos[0] - 1), min(pos[0] + 2, len(grid[0]))):
                    for new_j in range(max(0, pos[1] - 1), min(pos[1] + 2, len(grid[0]))):
                        if new_i == new_j:
                            continue
                        new[(new_i, new_j)] = max(new.get((new_i, new_j), 0),
                                                  memo[pos] + grid[row][new_i] + grid[row][new_j])
            memo = new
            row += 1
        return max(memo.values())


soln = Solution()
print(soln.cherryPickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
print(soln.cherryPickup([[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 3, 0], [2, 0, 9, 0, 0, 0, 0], [0, 3, 0, 5, 4, 0, 0],
                         [1, 0, 2, 3, 0, 0, 6]]))
print(soln.cherryPickup([[1, 0, 0, 3], [0, 0, 0, 3], [0, 0, 3, 3], [9, 0, 3, 3]]))
print(soln.cherryPickup([[1, 1], [1, 1]]))
print(soln.cherryPickup(
    [[8, 8, 10, 9, 1, 7], [8, 8, 1, 8, 4, 7], [8, 6, 10, 3, 7, 7], [3, 0, 9, 3, 2, 7], [6, 8, 9, 4, 2, 5],
     [1, 1, 5, 8, 8, 1], [5, 6, 5, 2, 9, 9], [4, 4, 6, 2, 5, 4], [4, 4, 5, 3, 1, 6], [9, 2, 2, 1, 9, 3]]))
