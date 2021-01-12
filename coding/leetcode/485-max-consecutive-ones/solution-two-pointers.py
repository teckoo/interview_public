class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums: return 0

        result = 0
        left, right = 0, 0
        length = len(nums)
        while right < length:
            num = nums[right]
            if num == 0:
                result = max(result, right - left)
                left = right + 1
            right += 1
        return max(result, right - left)
