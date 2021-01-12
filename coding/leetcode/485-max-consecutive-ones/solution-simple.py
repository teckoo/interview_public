class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums: return 0

        result = 0
        left = 0
        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                result = max(result, i - left)
                left = i + 1
        return max(result, i - left + 1)
