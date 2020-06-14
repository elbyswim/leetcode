from random import choices


class Solution:

    def __init__(self, w):
        self.w = w

    def pickIndex(self):
        return choices(range(len(self.w)), weights=self.w)[0]


soln = Solution([1, 3])
for i in range(5):
    print(soln.pickIndex())

