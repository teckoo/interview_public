# Runtime: 60 ms, faster than 98.76% of Python3 online submissions for Subtree of Another Tree.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Subtree of Another Tree.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def convert(p):
            return f"^{p.val}#{convert(p.left)}{convert(p.right)}" if p else "$"
        # print(convert(t))
        # print(convert(s))
        return convert(t) in convert(s)
