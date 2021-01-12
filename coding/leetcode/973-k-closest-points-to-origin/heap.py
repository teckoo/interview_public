# Runtime: 668 ms, faster than 89.61% of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 18.4 MB, less than 5.80% of Python3 online submissions for K Closest Points to Origin.

# keep a min-heap of -distance, size = k
# when a new item found smaller than current k-th item, pop current min
# and push the new item
#
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        cur_k = -100000000
        for x, y in points:
            d = -(x*x + y*y)
            if len(heap) < K:
                heapq.heappush(heap, (d, x, y))
                cur_k = min(cur_k, d)
                # print("init:", d, x, y)
            else:
                if d > cur_k:
                    # print("update:", d, x, y)
                    # print("pop: ", )
                    heapq.heappop(heap)
                    heapq.heappush(heap, (d, x, y))
                    cur_k = heap[0][0]

        return [(x, y) for (d, x, y) in heap]
