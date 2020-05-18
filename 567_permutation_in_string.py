class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        c1 = Counter(s1)
        c2 = Counter(s2[:len(s1)])
        for key in c2:
            c1[key] = c1.get(key, 0)

        for i in range(len(s2) - len(s1) + 1):
            if i != 0:
                c2[s2[i - 1]] -= 1
                c2[s2[i + len(s1) - 1]] = c2.get(s2[i + len(s1) - 1], 0) + 1
                c1[s2[i + len(s1) - 1]] = c1.get(s2[i + len(s1) - 1], 0)
            if c1 == c2:
                return True
        return False

soln = Solution()
print(soln.checkInclusion("aa", "baa"))