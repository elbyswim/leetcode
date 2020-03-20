class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right



def rangeSumBST(root, L, R):
    def rangeSumBSTNode(root, L, R):
        sum = 0
        if root.val in range(L, R + 1):
            sum += root.val
        if root.left:
            sum += rangeSumBSTNode(root.left, L, R)
        if root.right:
            sum += rangeSumBSTNode(root.right, L, R)
        return sum
    return rangeSumBSTNode(root, L, R)


testtree = TreeNode(10,
                    TreeNode(5,
                             TreeNode(3),
                             TreeNode(7)),
                    TreeNode(15,
                             None,
                             TreeNode(18)))

print(rangeSumBST(testtree, 7, 15))
