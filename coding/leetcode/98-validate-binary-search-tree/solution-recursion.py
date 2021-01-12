class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def is_valid(root, low, high):
            if not root: return True
            if root.val <= low or root.val >= high:
                return False
            return is_valid(root.left, low, root.val) and is_valid(root.right, root.val, high)
        return is_valid(root, float("-inf"), float("inf"))
