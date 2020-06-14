class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root):
        self.pals = 0

        def rec(root, odds, counter):
            counter[root.val] = counter.get(root.val, 0) + 1
            odds += 1 if counter[root.val] % 2 == 1 else -1
            if root.left is None and root.right is None:
                self.pals += 1 if odds < 2 else 0
                return
            else:
                odds1 = odds
                if root.left:
                    rec(root.left, odds, counter.copy())
                if root.right:
                    rec(root.right, odds1, counter.copy())

        rec(root, 0, {}, [])

        return self.pals


test1 = TreeNode(2, TreeNode(1, TreeNode(1), TreeNode(3, None, TreeNode(1))), TreeNode(1))

soln = Solution()
print(soln.pseudoPalindromicPaths(test1))
