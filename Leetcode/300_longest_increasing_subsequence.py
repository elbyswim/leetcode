class Solution:
    def lengthOfLIS(self, nums) -> int:
        memo = {}
        for num in nums:
            lis = list(map(lambda x: memo[x], filter(lambda x: x < num, memo.keys())))
            memo[num] = max(lis) if len(lis) > 0 else 0 + 1
        return max(memo.values())


soln = Solution()
test = [10, 9, 2, 5, 3, 7, 101, 18]
print(soln.lengthOfLIS(test))
