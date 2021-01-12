class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float("-inf")

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # if next element in inorder traversal is smaller
            # then it is not BST
            if root.val <= inorder: return False
            inorder = root.val
            root = root.right
        return True
