# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1

        prehead = ListNode(0)
        carry = 0
        cur = prehead
        # one of both lists has values
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            value = x + y + carry
            carry, mod = divmod(value, 10)
            node = ListNode(mod)
            cur.next = node
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # process shift digit and the rest
        if carry:
            cur.next = ListNode(carry)

        return prehead.next
