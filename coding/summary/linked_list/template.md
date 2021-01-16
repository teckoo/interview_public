# Reverse Linked list

## Iteration version

```python
def reverse(head):
    """ pre/cur/next, simplest solution """
    pre = None, cur = head
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre

def reverse(head):
    """ using dummy head is a trick to many linked list problems """
    if not head: return None
    dummy = ListNode()
    dummy.next = head
    while head.next:
        next = head.next
        head.next = next.next
        next.next = dummy.next
        dummy.next = next
    return dummy.next
```

![iteration version](./reverse_linkedlist_iteration.gif)

## Recursion version

```python
def reverse(ListNode head):
    if not head: return None
    if not head.next: return head
    last = reverse(head.next)
    head.next.next = head
    head.next = null
    return last
```

![recursion version](./reverse_linkedlist_recursion.jpg)