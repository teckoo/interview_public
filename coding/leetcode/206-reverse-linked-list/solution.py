# Runtime: 32 ms, faster than 89.84% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Reverse Linked List.

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # iteration version
        reversed = None
        while head:
            next = head.next
            head.next = reversed
            reversed = head
            head = next
        return reversed
        ####################
        # recursive version
        ####################
        # if head is None or head.next is None: 
            # return head
        # new_head = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return new_head
