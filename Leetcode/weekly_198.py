class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunk = empty = 0
        while numBottles + empty>= numExchange:
            drunk += numBottles # 16
            empty += numBottles # 15, 8
            numBottles = empty // numExchange # 1
            empty %= numExchange # 7
        drunk += numBottles
        return drunk

soln = Solution()
print(soln.numWaterBottles(15, 4))
print(soln.numWaterBottles(15, 8))
