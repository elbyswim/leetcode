class Solution:
    def jump(self, nums, start=0) -> int:
        pos = count = 0
        while pos != len(nums) - 1:
            next_pos = pos
            max_range = 0
            for i in range(min(nums[pos], len(nums) - pos - 1)):
                # if pos + i + 1 < len(nums) and max_range <= pos + i + 1 + nums[pos + i + 1]:
                if max_range <= pos + i + 1 + nums[pos + i + 1]:
                    max_range = pos + i + 1 + nums[pos + i + 1]
                    next_pos = pos + i + 1
            pos = next_pos
            count += 1
        return count


tests = [[2, 3, 1, 1, 4], [7, 9, 5, 2, 5, 7, 3, 8, 8, 7, 9, 3, 1, 7, 6, 3, 8, 7, 2, 2, 5, 9]]
soln = Solution()
print(soln.jump(tests[0]))
