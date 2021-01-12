# Runtime: 72 ms, faster than 86.56% of Python3 online submissions for Minimum Size Subarray Sum.
# Memory Usage: 15.1 MB, less than 7.69% of Python3 online submissions for Minimum Size Subarray Sum.
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        total = left = 0
        result = len(nums) + 1
        for right, n in enumerate(nums):
            total += n
            while total >= s:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0
