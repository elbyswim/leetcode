class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode, minimum=None, maximum=None) -> bool:
        if minimum is not None:
            if root.val <= minimum:
                return False
        if maximum is not None:
            if root.val >= maximum:
                return False
        if not (root.right or root.left):
            return True
        else:
            return (self.isValidBST(root.left, minimum, root.val) if root.left else True) and \
                   (self.isValidBST(root.right, root.val, maximum) if root.right else True)


soln = Solution()
test = TreeNode(0, None, TreeNode(-1))

print(soln.isValidBST(test))
