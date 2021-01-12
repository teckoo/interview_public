class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums or len(nums) < 3: return -1

        total = 0
        prefix = [0] * len(nums)
        for i, n in enumerate(nums):
            total += n
            prefix[i] = total
        # print(f"total = {total}")    
        for i in range(len(prefix)):
            if i == 0 and total - nums[0] == 0:
                return 0
            elif i > 0 and prefix[i-1] == total - prefix[i]:
                return i
        return -1
