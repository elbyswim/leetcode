class Solution:
    def getStrongest(self, arr, k: int):
        arr.sort()
        median = arr[(len(arr) - 1) // 2]
        arr.sort(key=lambda x: (-abs(x - median), -x))
        return arr[:k]


tests = [[[1, 2, 3, 4, 5], 2],
         [[1, 1, 3, 5, 5], 2],
         [[6, 7, 11, 7, 6, 8], 5],
         [[6, -3, 7, 2, 11], 3],
         [[-7, 22, 17, 3], 2], ]
soln = Solution()
for test in tests:
    print(soln.getStrongest(test[0], test[1]))

    [None, None, None, None, "facebook.com", "google.com", "facebook.com", None, "linkedin.com", "google.com",
     "leetcode.com"] == [None, None, None, None, "facebook.com", "google.com", "facebook.com", None, "linkedin.com",
                         "google.com", "leetcode.com"]
