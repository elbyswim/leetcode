class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None





def diameterOfBinaryTree(root):
    def treeheight(root):
        if root:
            return 1 + max(treeheight(root.left), treeheight(root.right))
        else:
            return 0

    if root:
        return max(self.diameterOfBinaryTree(root.left),
                   self.diameterOfBinaryTree(root.right),
                   1 + treeheight(root.left) + treeheight(root.right))
    else:
        return 0

    [1, 2, null, 4, 5, 6, null, 7]