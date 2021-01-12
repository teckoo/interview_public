# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# situ: this solution is easier to understand
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        while curr.next:
            next = curr.next
            curr.next = next.next
            next.next = dummy.next
            dummy.next = next
        return dummy.next
