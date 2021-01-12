# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy_odd = ListNode(0)
        dummy_even = ListNode(0)

        dummy_odd.next = head
        # process the list
        is_odd = True
        cur = dummy_odd  # start as odd
        odd = dummy_odd
        even = dummy_even
        while cur and cur.next:
            cur = cur.next
            if is_odd:
                odd.next = cur
                odd = odd.next
                # print("odd", cur.val)
            else:
                even.next = cur
                even = even.next
                # print("even", cur.val)
            is_odd = not is_odd
        # cur.next is None by now    
        # print("odd tail", cur.val)
        odd.next = dummy_even.next
        even.next = None
        return dummy_odd.next
