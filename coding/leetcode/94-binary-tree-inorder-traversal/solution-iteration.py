# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        result = []

        stack = collections.deque()
        node = root
        while node or stack:
            while node:
                # print(f"push {node.val}")
                stack.append(node)
                node = node.left

            node = stack.pop()
            result.append(node.val)
            # print(f"add to result: {node.val}")
            node = node.right

        return result
