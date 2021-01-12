# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        pre_head = ListNode(0)
        pre_head.next = head

        prev = pre_head
        curr = prev.next
        while curr and curr.next:
            first_node = curr
            second_node = curr.next

            # swap
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # next round
            prev = first_node
            curr = prev.next if prev else None
        return pre_head.next
