def maxSubArray(nums):
    def helper(nums):
        if len(nums) == 1:
            return nums[0]
        mid = len(nums) // 2
        left = helper(nums[:mid])
        right = helper(nums[mid:])
        center = max([sum(nums[i:mid]) for i in range(mid)]) + \
                 max([sum(nums[mid:i]) for i in range(mid + 1, len(nums) + 1)])
        return max(left, right, center)
    return helper(nums)


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
