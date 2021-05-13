class Solution:
    def findAnagrams(self, s: str, p: str):
        from collections import Counter
        pcounter = Counter(p)
        scounter = Counter(s[:len(p)])
        for key in scounter:
            pcounter[key] = pcounter.get(key, 0)
        idxs = []
        for i in range(len(s) - len(p) + 1):
            if i != 0:
                scounter[s[i - 1]] -= 1
                scounter[s[i + len(p) - 1]] = scounter.get(s[i + len(p) - 1], 0) + 1
                pcounter[s[i + len(p) - 1]] = pcounter.get(s[i + len(p) - 1], 0)
            if pcounter == scounter:
                idxs.append(i)
        return idxs


soln = Solution()
print(soln.findAnagrams("baa", "aa"))
