class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def in_left(m):
            return nums[0] <= target < nums[m] \
                    or nums[m] < nums[0] <= target \
                    or target < nums[m] < nums[0]

        if nums is None or len(nums) == 0: return -1

        l, r = 0, len(nums) - 1
        while l <= r: 
            m = l + (r - l) // 2
            
            if nums[m] == target: 
                return m
            elif in_left(m): 
                r = m - 1
            else:
                l = m + 1
            # print(f"m={m}, l={l}, r={r}, nums[m]={nums[m]}")
        return -1