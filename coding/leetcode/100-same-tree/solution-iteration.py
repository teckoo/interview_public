# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        queue = collections.deque([(p, q)])
        while queue:
            p, q = queue.popleft()
            if not p and not q: continue
            elif not p or not q: return False
            if p.val != q.val: return False
            queue.append((p.left, q.left))
            queue.append((p.right, q.right))

        return True
