class Solution:
    def largestNumber(self, cost, target: int) -> str:
        cost.reverse()
        coins = sorted(list(set(cost)))
        self.targetCoins = None
        self.dict =

        def dictSum(dict):
            ans = 0
            for k, v in dict:
                ans += k * v
            return ans



        seen = {}
        ans = ''
        if self.targetCoins:
            for coin in self.targetCoins:
                if coin not in seen:
                    seen[coin] = str(9 - cost.index(coin))
                ans += seen[coin]
            return ans
        else:
            return '0'


soln = Solution()

print(soln.largestNumber([4, 3, 2, 5, 6, 7, 2, 5, 5], 4999))
print(soln.largestNumber([7, 6, 5, 5, 5, 6, 8, 7, 8], 12))
print(soln.largestNumber([2, 4, 6, 2, 4, 6, 4, 4, 4], 5))
print(soln.largestNumber([6, 10, 15, 40, 40, 40, 40, 40, 40], 47))
