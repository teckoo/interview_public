class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        items = {}
        for idx, num in enumerate(nums):
            if num in items and idx - items[num] <= k:
                return True
            else:
                items[num] = idx
        return False
