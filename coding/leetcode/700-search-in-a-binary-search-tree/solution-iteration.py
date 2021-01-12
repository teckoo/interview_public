# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return None
        while root and root.val != val:
            if val < root.val:
                root = root.left
            else:
                root = root.right
        return root
