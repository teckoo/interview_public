# Runtime: 24 ms, faster than 89.42% of Python3 online submissions for Same Tree.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Same Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None: return True
        if p is None or q is None: return False

        return p.val == q.val \
                and self.isSameTree(p.left, q.left) \
                and self.isSameTree(p.right, q.right)
