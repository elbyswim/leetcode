# Definition for a binary tree node.
from itertools import permutations


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int):
        def insertNode(root, node):
            cur = root
            if root:
                while True:
                    if node < cur.val:
                        if cur.left:
                            cur = cur.left
                        else:
                            cur.left = TreeNode(node)
                            break
                    else:
                        if cur.right:
                            cur = cur.right
                        else:
                            cur.right = TreeNode(node)
                            break
            else:
                root = TreeNode(node)
            return root

        def generateTree(nums):
            tree = None
            for n in nums:
                tree = insertNode(tree, n)
            return tree

        trees = set()
        for perm in permutations(range(1, n + 1)):
            trees.add(generateTree(perm))
        return list(trees)

def levelOrderTraversal(root):
    from collections import deque
    queue = deque()
    queue.append(root)
    traversal = []
    while len(queue) > 0:
        node = queue.popleft()
        traversal.append(node.val if node else node)
        if node:
            if node.left or node.right:
                queue.append(node.left)
                queue.append(node.right)
    return traversal


soln = Solution()
print([levelOrderTraversal(tree) for tree in soln.generateTrees(3)])
