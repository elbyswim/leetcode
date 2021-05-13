class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        while num % 2 == 0:
            num //= 2
            print(num)
        while num % 3 == 0:
            num //= 3
            print(num)
        while num % 5 == 0:
            num //= 5
            print(num)
        return num == 1

soln = Solution()
for i in range(5, 11):
    print('num = {}'.format(i))
    soln.isUgly(i)