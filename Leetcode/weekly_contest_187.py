import random
from functools import reduce


class Solution:
    def longestSubarray(self, nums, limit):
        memo1 = [0 for _ in range(len(nums))]
        memo2 = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            j = 1
            while i + j < len(nums):
                if nums[i] - limit <= nums[i + j] <= nums[i]:
                    j += 1
                else:
                    break
            memo1[i] = j - 1
        for i in range(len(nums) - 1, -1, -1):
            j = 1
            while i - j > -1:
                if nums[i] - limit <= nums[i - j] <= nums[i]:
                    j += 1
                else:
                    break
            memo2[i] = j - 1
        return max([1 + memo1[i] + memo2[i] for i in range(len(nums))])

    def kthSmallest(self, mat, k: int) -> int:
        ksum = sum(mat[i][0] for i in range(len(mat)))
        if len(mat[0]) == 1:
            return k
        diffs = {}
        lastdiff = 0
        for i in range(len(mat)):
            diffs[i] = (1, mat[i][1] - mat[i][0])
        for _ in range(k):
            mindiff = min(diffs.values())
            for i in diffs:
                if diffs[i] == mindiff:
                    index = i
                    break
            ksum = ksum + diffs[index][1] - lastdiff
            lastdiff = diffs[index][1]
            if diffs[index][0] < len(mat[0]) - 2:
                diffs[index] = (diffs[index][0] + 1, mat[index][diffs[index][0] + 1] - mat[index][0])
            else:
                diffs.pop(index)
        return ksum

    def longestSubarray1(self, nums, limit):
        memo1 = [0 for _ in range(len(nums))]
        memo2 = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            j = 1
            mini = maxi = nums[i]
            while maxi - mini <= limit and i + j < len(nums):
                mini = min(mini, nums[i + j])
                maxi = max(maxi, nums[i + j])
                j += 1
            memo1[i] = j - (1 if maxi - mini > limit else 0)
        return max(memo1)


tests = [[[8, 2, 4, 7], 4],
         [[10, 1, 2, 4, 7, 2], 5],
         [[4, 2, 2, 2, 4, 4, 2, 2], 0],
         [[random.randint(1, 10 ** 9) for _ in range(10 ** 5)], random.randint(0, 10 ** 9)]]

# tests = [
#     [[[1, 3, 11], [2, 4, 6]], 5],
#     [[[1, 3, 11], [2, 4, 6]], 9],
#     [[[1, 10, 10], [1, 4, 5], [2, 3, 6]], 7],
#     [[[1, 1, 10], [2, 2, 9]], 7]
# ]

soln = Solution()
for test in tests:
    print(test)
    print(soln.longestSubarray1(test[0], test[1]))
