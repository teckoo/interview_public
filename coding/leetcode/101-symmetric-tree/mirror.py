# Runtime: 28 ms, faster than 88.50% of Python3 online submissions for Symmetric Tree.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Symmetric Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def is_mirror(s, t) -> bool:
            if s is None and t is None: return True
            if s is None or t is None: return False
            return s.val == t.val \
                    and is_mirror(s.left, t.right) \
                    and is_mirror(s.right, t.left)
        return is_mirror(root, root)

