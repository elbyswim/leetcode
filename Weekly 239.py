from random import randint


#
# print(intervals)

class Solution:
    def splitString(self, s: str) -> bool:
        def rec(s, start):
            print(s, start)
            if len(s) == 0:
                return False
            i = 1
            if start - 1 == int(s):
                return True
            while i < len(s) and start >= int(s[:i]):
                if start - 1 == int(s[:i]):
                    return rec(s[i:], int(s[:i]))
                i += 1
            return False
        i = 1
        while i < len(s):
            print('next try')
            if rec(s[i:], int(s[:i])):
                return True
            i += 1
        return False

    def minInterval(self, intervals, queries):
        min_intervals = {}
        for interval in intervals:
            size = interval[1] - interval[0] + 1
            for i in range(interval[0], interval[1] + 1):
                if i in min_intervals:
                    min_intervals[i] = min(min_intervals[i], size)
                else:
                    min_intervals[i] = size
        for i in range(len(queries)):
            queries[i] = min_intervals[queries[i]] if queries[i] in min_intervals else -1
        return queries


s = Solution()
# print(s.splitString('1234'))
# print(s.splitString('050043'))
# print(s.splitString('9080701'))
# print(s.splitString('10009998'))


intervals = []

for i in range(100000):
    a, b = randint(0, 10 ** 7), randint(0, 10 ** 7)
    intervals.append([min(a, b), max(a, b)])
queries = [2,3,4,5]

print(s.minInterval(intervals, queries))