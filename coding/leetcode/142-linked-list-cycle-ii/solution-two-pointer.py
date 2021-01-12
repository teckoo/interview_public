# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def meet(self, head: ListNode) -> ListNode:
        if not head: return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            # print(slow.val, fast.val)
            if slow == fast: return slow
        return None

    def detectCycle(self, head: ListNode) -> ListNode:
        fast = self.meet(head)
        if not fast: return None
        slow = head
        while slow != fast:
            # print(slow.val, fast.val)
            if not fast or not fast.next: return None
            slow = slow.next
            fast = fast.next

        return slow
