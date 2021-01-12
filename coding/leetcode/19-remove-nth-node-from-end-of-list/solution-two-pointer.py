# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        for _ in range(n): fast = fast.next
        # print('fast', fast.val)    
        while fast.next:
            fast = fast.next
            slow = slow.next
        # remove the n-th node using slow ptr
        # print('slow', slow.val)    
        slow.next = slow.next.next
        return dummy.next
