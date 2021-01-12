# Runtime: 44 ms, faster than 21.82% of Python3 online submissions for Copy List with Random Pointer.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Copy List with Random Pointer.
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def __init__(self):
        self.visited = {}
        
    def clone_node(self, node):
        if node is None: 
            return None
        elif node in self.visited:
            return self.visited[node]
        
        new_node = Node(node.val)
        self.visited[node] = new_node
        return new_node
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None: 
            return None
        
        old_node = head
        new_node = Node(head.val)
        self.visited[head] = new_node
        
        while old_node:
            new_node.next = self.clone_node(old_node.next)
            new_node.random = self.clone_node(old_node.random)
            
            old_node = old_node.next
            new_node = new_node.next
            
        return self.visited[head]
