# Runtime: 28 ms, faster than 88.16% of Python3 online submissions for Reverse Linked List II.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Reverse Linked List II.
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None or head.next is None:
            return head
        
        pre = ListNode(0)
        pre.next = head
        new_head = pre
        
        i = 1
        while i < m:
            pre = pre.next
            i += 1
        
        cur = pre.next
        while i < n:
            t = cur.next
            cur.next = t.next
            t.next = pre.next
            pre.next = t
            i += 1
            
        return new_head.next
