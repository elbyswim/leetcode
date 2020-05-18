class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        for i in range(k):
            if num == '0':
                break
            smallest = int(num)
            for j in range(len(num)):
                smallest = min(smallest, int(num[:j] + num[j + 1:]))
            num = str(smallest)
        return num


soln = Solution()
print(soln.removeKdigits('10', 2))
