class Solution:
    def kthFactor(self, n, k):
        i = int(n ** 0.5)
        factors = []
        while i > 0:
            if not n % i:
                if n // i != i:
                    factors = [i] + factors + [n // i]
                else:
                    factors = [i]
            i -= 1
        if k <= len(factors):
            return factors[k - 1]
        else:
            return -1

    def longestSubarray(self, nums):
        new = cont = long = 0
        for i, num in enumerate(nums):
            if num == 1:
                new += 1
                cont += 1
            else:
                cont, new = new, 0
            long = max(long, cont)
        if long == len(nums):
            long -= 1
        return long


soln = Solution()


tests = [
    # [1, 1, 0, 1],
    # [0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1],
    # [1, 1, 0, 0, 1, 1, 1, 0, 1],
    # [0, 0, 0]
]
# print(soln.kthFactor(12, 3))
for test in tests:
    print(soln.longestSubarray(test))
