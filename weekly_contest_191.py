class Solution:
    def minReorder(self, n: int, connections):
        from collections import deque
        edges = {i: {'in': set(), 'out': set()} for i in range(n)}
        for conn in connections:
            edges[conn[0]]['out'].add(conn[1])
            edges[conn[1]]['in'].add(conn[0])
        queue = deque([0])
        seen = set()
        count = 0
        while len(queue) > 0:
            curr = queue.popleft()
            for conn in edges[curr]['in']:
                if conn not in seen:
                    queue.append(conn)
            for conn in edges[curr]['out']:
                if conn not in seen:
                    queue.append(conn)
                    count += 1
        return count

    def getProbability(self, balls) -> float:
        from itertools import permutations
        n = sum(balls)
        allBalls = []
        for i, count in enumerate(balls):
            allBalls += [i] * count
        perms = set(permutations(allBalls, len(allBalls)))
        count = 0
        for perm in perms:
            count += 1 if len(set(perm[:n // 2])) == len(set(perm[n // 2:])) else 0
        return count / len(perms)


soln = Solution()
tests = [
    [1, 1],
    [2, 1, 1],
    [1, 2, 1, 2],
    [3, 2, 1],
    [6, 6, 6, 6, 6, 6, 6, 6]]
# for test in tests

# print(soln.getProbability(tests[4]))

from math import factorial, comb
from itertools import combinations, permutations

count = factorial(sum(tests[4]))
for i in tests[4]:
    count //= factorial(i)
print(count)

balls = tests[3]
allBalls = []
for i, count in enumerate(balls):
    allBalls += [i] * count
print(allBalls)
print(list(combinations(allBalls, sum(balls) // 2)))
