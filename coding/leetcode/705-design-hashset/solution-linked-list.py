class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_range = 769
        self.bucket_array = [Bucket() for _ in range(self.key_range)]

    def _hash(self, key):
        return key % self.key_range
    
    def add(self, key: int) -> None:
        bucket_index = self._hash(key)
        self.bucket_array[bucket_index].insert(key)

    def remove(self, key: int) -> None:
        bucket_index = self._hash(key)
        self.bucket_array[bucket_index].delete(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucket_index = self._hash(key)
        return self.bucket_array[bucket_index].exists(key)


class Node:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.next = nextNode
        
        
class Bucket:
    def __init__(self):
        self.head = Node(0)  # pseudo head
        
    def insert(self, value):
        """ insert at the beginning """
        if not self.exists(value):
            node = Node(value, self.head.next)
            self.head.next = node 
            
    def delete(self, value):
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.value == value:
                # remove the current node
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
            
    def exists(self, value):
        curr = self.head.next
        while curr:
            if curr.value == value:
                # value exists already, do nothing
                return True
            curr = curr.next
        return False
    
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
