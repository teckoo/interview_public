import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            if len(h) < k:
                heapq.heappush(h, n)
            else:
                heapq.heappushpop(h, n)
        return heapq.heappop(h)
