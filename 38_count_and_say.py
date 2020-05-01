class Solution:
    def countAndSay(self, n: int) -> str:
        number = '1'
        while n > 1:
            new = ''
            first = last = 0
            while last < len(number):
                if number[first] != number[last]:
                    new += str(last - first)
                    new += str(number[first])
                    first = last
                last += 1
                if last == len(number):
                    new += str(last - first)
                    new += str(number[first])
            number = new
            n -= 1
        return number


soln = Solution()
for i in range(1, 10):
    print(soln.countAndSay(i))
