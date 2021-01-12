import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return None

        def partition(lo, hi, pv):
            """ given an index of pv (0-based),
            return the rank of this item after sort
            """
            # 1. move pv to the end
            n = nums[pv]
            nums[hi], nums[pv] = nums[pv], nums[hi]

            # 2. move larger item to the left.
            pos = lo
            for i in range(lo, hi):
                if nums[i] > n:
                    nums[pos], nums[i] = nums[i], nums[pos]
                    pos += 1
            nums[pos], nums[hi] = nums[hi], nums[pos]
            return pos

        def quickselect(lo, hi, k):
            """ return the k-largest (0 based) item in the list """
            if lo == hi: return nums[lo]

            pivot = random.randint(lo, hi)
            pos = partition(lo, hi, pivot)
            if pos == k: return nums[k]
            elif pos > k:
                return quickselect(lo, pos - 1, k)
            else:
                return quickselect(pos + 1, hi, k)

        return quickselect(0, len(nums) - 1, k - 1)
