class Solution:
    def change(self, amount: int, coins) -> int:
        memo = [0 for _ in range(amount + 1)]
        memo[0] = 1
        for coin in coins:
            for i in range(amount):
                if i + 1 - coin >= 0:
                    memo[i + 1] += memo[i + 1 - coin]
        return memo[-1]

soln = Solution()
print(soln.change(5, [1, 2, 5]))
