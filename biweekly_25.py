class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        l1 = list(map(lambda c: ord(c), sorted(s1)))
        l2 = list(map(lambda c: ord(c), sorted(s2)))
        for i in range(len(l1)):
            l1[i] -= l2[i]
        return len(list(filter(lambda x: x >= 0, l1))) == len(l1) or len(list(filter(lambda x: x <= 0, l1))) == len(l1)

    def maxDiff(self, num: int) -> int:
        def smallest(num):
            string = str(num)
            int1 = int(string.replace(string[0], '1'))
            x = None
            int2 = num
            for c in string:
                if c not in {string[0], '0'}:
                    x = c
                    break
            if x is not None:
                int2 = int(string.replace(x, '0'))
            return min(int1, int2)

        def largest(num):
            string = str(num)
            int1 = int(string.replace(string[0], '9'))
            x = None
            int2 = num
            for c in string:
                if c != string[0]:
                    x = c
                    break
            if x is not None:
                int2 = int(string.replace(x, '9'))
            return max(int1, int2)

        a = smallest(num)
        b = largest(num)
        return b - a

    def numberWays(self, hats, used=set()) -> int:
        if len(hats) == 1:
            return len(list(filter(lambda x: x not in used, hats[0])))
        else:
            totalways = 0
            for h in hats[0]:
                if h not in used:
                    totalways += self.numberWays(hats[1:], used.union({h}))
            return totalways % (10 ** 9 + 7)

    def numberWays1(self, hats, used=set()) -> int:
        from itertools import product
        combos = list(filter(lambda x: len(set(x)) == len(hats), list(product(*hats))))
        return len(combos)



soln = Solution()
test1 = [list(range(1, 41)) for _ in range(10)]
tests = [[[3, 4], [4, 5], [5]],
         [[3, 5, 1], [3, 5]],
         [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
         [[1, 2, 3], [2, 3, 5, 6], [1, 3, 7, 9], [1, 8, 9], [2, 5, 7]]
    , test1

         ]
for test in tests:
    print(soln.numberWays1(test))
