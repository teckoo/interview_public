/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode MergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head, curNode;
        try
        {
            if (l1.val < l2.val)
            {
                head = l1;
                l1 = l1.next;
            } else
            {
                head = l2;
                l2 = l2.next;
            }
        } catch (Exception e)
        {
            if (l1 != null) { head = l1; }
            else if (l2 != null) { head = l2;}
            else return null;
            return head;
        }
        curNode = head;
        while (l1 != null && l2 != null)
        {
            if (l1.val < l2.val)
            {
                curNode.next = l1;
                l1 = l1.next;
            } else 
            {
                curNode.next = l2;
                l2 = l2.next;
            }
            curNode = curNode.next;
        }
        if (l1 == null){
            curNode.next = l2;
        } else
        {
            curNode.next = l1;
        }
        return head;
    }
}
