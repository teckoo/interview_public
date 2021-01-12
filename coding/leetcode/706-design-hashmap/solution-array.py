class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cnt = 1000
        self.bucket = [None] * self.cnt

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.cnt
        item = self.bucket[idx]
        if item is None:
            self.bucket[idx] = [[key, value]]
        else:
            for i in item:
                if key == i[0]:
                    i[1] = value
                    return
            item.append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % self.cnt
        item = self.bucket[idx]
        if item:
            for k, v in item:
                if k == key: return v
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = key % self.cnt
        item = self.bucket[idx]
        if item:
            for pos, i in enumerate(item):
                if i[0] == key: 
                    del item[pos]
                    return

