# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        nodes = set()
        cur = head
        while cur:
            if cur in nodes: return True
            nodes.add(cur)
            cur = cur.next
        return False
