# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        
        result = []
        level_list = deque()
        node_queue = deque([root, None])
        is_order_left = True
        
        while len(node_queue) > 0:
            cur_node = node_queue.popleft()
            
            if cur_node:
                if is_order_left:
                    level_list.append(cur_node.val)
                else:
                    level_list.appendleft(cur_node.val)
                    
                if cur_node.left:
                    node_queue.append(cur_node.left)
                if cur_node.right:
                    node_queue.append(cur_node.right)
            else:
                result.append(level_list)
                if len(node_queue) > 0:
                    node_queue.append(None)
                
                # print(f"{level_list}, {is_order_left}, {node_queue}")
                level_list = deque()
                is_order_left = not is_order_left
        
        return result
