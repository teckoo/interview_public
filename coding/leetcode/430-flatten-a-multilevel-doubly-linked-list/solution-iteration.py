"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return head

        prehead = Node(None, None, head, None)
        prev = prehead

        stack = []
        stack.append(head)

        while stack:
            cur = stack.pop()
            prev.next = cur
            cur.prev = prev

            if cur.next:
                stack.append(cur.next)

            if cur.child:
                stack.append(cur.child)
                cur.child = None

            prev = cur

        # detach prehead from the result
        prehead.next.prev = None
        return prehead.next
