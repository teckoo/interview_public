from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = deque()
        self.win_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.count += 1
        head = self.queue.popleft() if self.count > self.size else 0
        self.win_sum = self.win_sum - head + val
        if self.count > self.size:
          self.count = self.size
        return self.win_sum / self.count


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
