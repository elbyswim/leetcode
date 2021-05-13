class Solution:

    def avoidFlood(self, rains):
        ans = [1] * len(rains)
        full = {}
        empty = []
        for day, rain in enumerate(rains):
            if rain == 0:
                empty.append(day)
            elif rain > 0:
                ans[day] = -1
                if rain in full:
                    if len(empty) == 0 or full[rain] > empty[-1]:
                        return []
                    else:
                        i = len(empty) - 1
                        last = full.pop(rain)
                        while True:
                            if i == 0 or empty[i - 1] < last:
                                break
                            else:
                                i -= 1
                        ans[empty.pop(i)] = rain
                full[rain] = day
        return ans


soln = Solution()
tests = [
    # [1, 2, 3, 4],
    # [1, 2, 0, 0, 2, 1],
    # [1, 2, 0, 1, 2],
    # [69, 0, 0, 0, 69],
    # [10, 20, 20],
    # [1, 0, 2, 3, 0, 1, 2],
    [1, 0, 1, 0, 2, 0, 2],
    [2, 3, 0, 0, 3, 1, 0, 1, 0, 2, 2]
]
for test in tests:
    print(soln.avoidFlood(test))
