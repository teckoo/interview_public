# Runtime: 180 ms, faster than 94.22% of Python3 online submissions for LRU Cache.
# Memory Usage: 22 MB, less than 27.27% of Python3 online submissions for LRU Cache.

from collections import OrderedDict

class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.cap = capacity


    def get(self, key: int) -> int:
        # print(f"get(): {key}, {self.arr}, {self.map},")
        
        val = self[key] if key in self else -1
        # print(f"{val}")
        if val > -1:
            self.move_to_end(key)
        return val

    def put(self, key: int, value: int) -> None:
        print(f"put() init: {key}, {self}")
        if key in self:
            self.move_to_end(key)
        self[key] = value
        
        if len(self) > self.cap:
            self.popitem(last = False)
            # print(f"put(): {key}, {pop_key}, {self.arr}, {self.map},")



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
