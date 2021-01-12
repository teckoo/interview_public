class Solution:
    """
    Runtime: 48 ms, faster than 93.84% of Python3 online submissions for Search Insert Position.
Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Search Insert Position.
    """
    def searchSet(self, nums: List[int], target: int, 
            low_bound: int, high_bound: int)-> int:

        if low_bound == high_bound-1: # only one item
            return high_bound if nums[low_bound] < target else low_bound

        m = low_bound + (high_bound - low_bound) // 2
        if nums[m] == target:
            return m

        if nums[m] < target:
            low_bound = m
        else:
            high_bound = m
        return self.searchSet(nums, target, low_bound, high_bound)

    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        return self.searchSet(nums, target, 0, len(nums))
