# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# This is not exact tail-recursion as help return is max(...) instead of helper().
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def helper(node, depth):
            if not node: return depth
            return max(helper(node.left, depth + 1),  helper(node.right, depth + 1))
        return helper(root, 0)
