from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0 
        que = deque()
        que.append(root)
        depth = 1
        while que:
            sz = len(que)
            for _ in range(sz):
                cur = que.popleft()
                if not cur.left and not cur.right:
                    # print(f"node val={cur.val}, {depth}")
                    return depth
                if cur.left:
                    # print(f"add val={cur.left.val}, {depth}")
                    que.append(cur.left)
                if cur.right:
                    # print(f"add val={cur.right.val}, {depth}")
                    que.append(cur.right)
            depth += 1
        return depth