class Solution:
    def largestDivisibleSubset(self, nums):
        from math import gcd
        def lcm(a, b):
            return a * b / gcd(a, b)

        if len(nums) == 0:
            return []
        subsets = []
        for num in nums:
            new = []
            for subset in subsets:
                if not (num % subset[1] and subset[2] % num):
                    new.append((subset[0] + [num], max(num, subset[1]), min(num, subset[2])))
            subsets.extend(new)
            if not len(new):
                subsets.append(([num], num, num))
        long = []
        for subset in subsets:
            if len(subset[0]) > len(long):
                long = subset[0]
        return long


soln = Solution()
print(soln.largestDivisibleSubset([1, 2, 3]))
