# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(node):
            if not node: return 0
            return 1 + max(depth(node.left), depth(node.right))
        if not root: return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and \
           abs(depth(root.left) - depth(root.right)) < 2
