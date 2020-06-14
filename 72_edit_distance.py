class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        memo = [0 for _ in range(len(word2))]
        for i in range(len(word1)):
            new = [0 for _ in range(len(word2))]
            for j in range(len(word2)):
                if i == 0 and j == 0:
                    memo[j] = 0 if word1[i] == word2[j] else 1
                elif i == 0:
                    memo[j] = min(memo[j - 1] + 1, j + (0 if word1[i] == word2[j] else 1))
                elif j == 0:
                    new[j] = min(memo[j] + 1, i + (0 if word1[i] == word2[j] else 1))
                else:
                    new[j] = min(new[j - 1] + 1,
                                 memo[j] + 1,
                                 memo[j - 1] + (0 if word1[i] == word2[j] else 1))
            memo = new
        return memo[-1]


soln = Solution()
print(soln.minDistance('horse', 'ros'))