class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_lb(l, r):
            """ return lower bound of the target """
            while l < r: 
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else: 
                    r = m
            return l if nums[l] == target else -1

        def find_ub(l, r):
            """ return upper bound of the target """
            while l < r: 
                m = (l + r + 1) // 2
                if nums[m] > target:
                    r = m - 1
                else: 
                    l = m
            return l if nums[l] == target else -1

        if nums is None or len(nums) == 0: return (-1, -1)

        lb = find_lb(0, len(nums) - 1)
        if lb == -1: return (-1, -1)
        ub = find_ub(lb, len(nums) - 1)
        return (lb, ub)
