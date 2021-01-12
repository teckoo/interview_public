class Solution:

    
    def searchSet(self, nums: List[int], target: int, low_bound: int, high_bound: int)-> int:
        # print(f"l={low_bound}, h={high_bound}")

        if low_bound == high_bound-1: # only one item
            return low_bound if nums[low_bound] >= target else high_bound
            
        m = low_bound + (high_bound - low_bound)//2
        if nums[m] == target:
            return m
         
        if nums[m] < target:
            low_bound = m
            return self.searchSet(nums, target, low_bound, high_bound)
        else:
            high_bound = m
            return self.searchSet(nums, target, low_bound, high_bound)

    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        return self.searchSet(nums, target, 0, len(nums))     
 
