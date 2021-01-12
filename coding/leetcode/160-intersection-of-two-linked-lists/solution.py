# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None
        pA = headA
        pB = headB
        firstA = firstB = True 
        while pA != pB:
            pA = pA.next
            pB = pB.next
            if not pA and firstA: 
                pA = headB 
                firstA = False 
            if not pB and firstB: 
                pB = headA
                firstB = False 
                
            if not pA or not pB: return None
            # print(pA.val, pB.val)    
        return pA
