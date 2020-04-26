class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0] * len(text2)] * len(text1)
        for k in range(len(text1) + len(text2) - 1):
            i = min(len(text1), k)
            j = k - i
            while i >= 0 and j < len(text2):
                if i == 0 and j == 0:
                    memo[i][j] = 1 if text1[i] == text2[j] else 0
                elif i == 0:
                    memo[i][j] = max(memo[i][j - 1], 1 if text1[i] == text2[j] else 0)
                elif j == 0:
                    memo[i][j] = max(memo[i - 1][j], 1 if text1[i] == text2[j] else 0)
                else:
                    memo[i][j] = memo[i - 1][j - 1] + 1 if text1[i] == text2[j] else max(memo[i - 1][j], memo[i][j - 1])
                i -= 1
                j += 1
        return memo[len(text1) - 1][len(text2) - 1]


soln = Solution()
print(soln.longestCommonSubsequence('abcde', 'ace'))
