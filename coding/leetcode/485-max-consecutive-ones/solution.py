class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums: return 0

        result = 0
        left = 0
        for i, n in enumerate(nums):
            if n == 0:
                # check result, update, adjust left, and cur_len
                result = max(result, i - left)
                left = i + 1
            elif i == len(nums)-1:
                result = max(result, i - left + 1)

        return result

    # NOTE: a shorter one can be:
    # 1. remove elif block
    # 2. return max(result, i-left+1)
