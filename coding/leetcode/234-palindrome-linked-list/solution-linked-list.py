class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None: return True

        # find the end of first half and reverse second half
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # check whether or not there is a palindrom
        result = True
        first_position = head
        second_position = second_half_start
        while result and not second_position:
            if first_position.val != second_position.val: 
                result = False
                break
            first_position = first_position.next
            second_position = second_position.next
        # reverse the second half and return
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while not fast.next and not fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        prev = None
        current = head
        while not current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
