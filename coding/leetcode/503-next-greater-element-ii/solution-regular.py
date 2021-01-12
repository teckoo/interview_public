class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        def find_next(num, idx):
            i = idx + 1
            if i >= len(nums): i = 0
            while i != idx:
                # print(f"{i}")
                if nums[i] > num:
                    return nums[i]
                i += 1
                if i >= len(nums): i = 0
            return -1
        
        ans = []
        
        for i, n in enumerate(nums):
            ans.append(find_next(n, i))
            
        return ans
