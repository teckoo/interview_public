# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur and cur.next:
            next = cur.next
            if next.val == val:
                cur.next = next.next
            else:
                cur = cur.next
        return dummy.next
