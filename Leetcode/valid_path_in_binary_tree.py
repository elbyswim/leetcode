class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr, i=0):
        if (not root) and i >= len(arr):
            return True
        if root and i < len(arr):
            if root.val == arr[i]:
                return self.isValidSequence(root.left, arr, i + 1) or self.isValidSequence(root.right, arr, i + 1)
        return False


test = TreeNode(0,
                TreeNode(1,
                         TreeNode(0, None, TreeNode(1)),
                         TreeNode(1, TreeNode(0), TreeNode(0))),
                TreeNode(0, TreeNode(0)))
soln = Solution()
print(soln.isValidSequence(test, [0, 1, 0, 1]))
