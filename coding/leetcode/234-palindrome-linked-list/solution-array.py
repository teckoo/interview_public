class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return True
        cur = head
        data = []
        while cur:
            data.append(cur.val)
            cur = cur.next

        size = len(data)
        for i in range(size // 2):
            if data[i] != data[size - 1 - i]: return False

        return True
