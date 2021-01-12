# Runtime: 32 ms, faster than 80.81% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# recursion version
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None: return l2
        elif l2 is None: return l1
        elif l1.val < l2.val:
            small = l1
            big = l2
        else:
            small = l2
            big = l1
        
        small.next = self.mergeTwoLists(small.next, big)
        return small
