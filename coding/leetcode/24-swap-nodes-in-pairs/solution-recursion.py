# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        first = head
        new_head = head.next
        rest = new_head.next
        new_head.next = first
        first.next = self.swapPairs(rest)
        return new_head
