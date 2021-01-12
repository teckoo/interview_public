# Runtime: 192 ms, faster than 79.96% of Python3 online submissions for Find Median from Data Stream.
# Memory Usage: 23.6 MB, less than 46.67% of Python3 online submissions for Find Median from Data Stream.

from heapq import *


class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
            # print("small==large:", self.small, self.large)
        else:
            heappush(self.small, -heappushpop(self.large, num))
            # print("small<large:", self.small, self.large)


    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
