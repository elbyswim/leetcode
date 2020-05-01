class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root):
        def helper(root1, root2):
            root2.val = root1.val
            left = right = 0
            if root1.left:
                root2.left = TreeNode()
                left = helper(root1.left, root2.left)
            if root1.right:
                root2.right = TreeNode()
                right = helper(root1.right, root2.right)
            root2.val += max(0, left, right)
            return root2.val

        def helper2(root1, root2, root3):
            root3.val = root1.val
            pathSum = root1.val
            if root1.left:
                pathSum += max(0, root2.left.val)
                root3.left = TreeNode()
                root3.val = max(root3.val, helper2(root1.left, root2.left, root3.left))
            if root1.right:
                pathSum += max(0, root2.right.val)
                root3.right = TreeNode()
                root3.val = max(root3.val, helper2(root1.right, root2.right, root3.right))
            root3.val = max(root3.val, pathSum)
            return root3.val
        root2 = TreeNode()
        root3 = TreeNode()
        helper(root, root2)
        return helper2(root, root2, root3)


test = TreeNode(-2, None, TreeNode(-3))
soln = Solution()
print(soln.maxPathSum(test))
