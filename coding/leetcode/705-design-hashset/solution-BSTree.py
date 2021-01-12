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

        
class Bucket:
    def __init__(self):
        self.tree = BSTree()
        
    def insert(self, value):
        """ insert at the beginning """
        self.tree.root = self.tree.insertIntoBST(self.tree.root, value)
            
    def delete(self, value):
        self.tree.root = self.tree.deleteNode(self.tree.root, value)
            
    def exists(self, value):
        return (self.tree.searchBST(self.tree.root, value) is not None)
    
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = self.right = None
        
        
class BSTree:
    def __init__(self):
        self.root = None
        
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or val == root.val:
            return root
        
        return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)
    
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        elif val == root.val:
            return root
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root
    
    def successor(self, root):
        """ one step right and then always left"""
        root = root.right
        
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root):
        """ one step left and then always right"""
        root = root.left
        while root.right:
            root = root.right
        return root.val
    
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return None
        
        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:  
                # node is not a leaf, has no right child, and have a left child
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
