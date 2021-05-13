import copy


class Solution:
    def prisonAfterNDays(self, cells, N):
        seen = []
        for _ in range(min(N, 14)):
            new = [None for _ in range(8)]
            for i in range(1, len(cells) - 1):
                new[i] = 1 if new[-1][i - 1] == new[-1][i + 1] else 0
            new[0] = new[-1] = 0
            seen.append(copy.deepcopy(new))
        if N <= 14:
            return seen[-1]
        else:
            print(seen)
            return seen[(N - 1) % 14]


soln = Solution()
print(soln.prisonAfterNDays([1, 0, 0, 1, 0, 0, 1, 0], 15))
