"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return head

        prehead = Node(None, None, head, None)
        self.flatten_dfs(prehead, head)

        # detach the prehead from the real head
        prehead.next.prev = None
        return prehead.next

    def flatten_dfs(self, prev, cur):
        """ return the tail of the flatten list """
        if not cur: return prev

        cur.prev = prev
        prev.next = cur

        # the cur.next would be tempered in the recursive function
        next = cur.next
        tail = self.flatten_dfs(cur, cur.child)
        cur.child = None
        return self.flatten_dfs(tail, next)
