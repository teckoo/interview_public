import unittest


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None: 
            return True
        if root.left.val != root.right.val:
            return False
        return self.isChildrenSymmetric(root.left, root.right)

    def isChildrenSymmetric(self, left: TreeNode, 
            right: TreeNode) -> bool:
        if left.val != right.val:
            return False
        return self.isChildrenSymmetric(left.left, right.right) and self.isChildrenSymmetric(left.left, right.right)


class MainTest(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        self.assertTrue(s.isSymmetric(t))


if __name__ == "__main__":
    s = Solution()
    s.isSymmetric(t)
