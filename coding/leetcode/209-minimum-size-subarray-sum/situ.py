class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        max_len = len(nums)
        if max_len == 0: return 0
        min_len = len(nums) + 1
        left = 0
        cur_sum = 0
        while left < max_len:
            for i in range(left + 1, max_len):
                if (i-left+1) >= min_len: break
                cur_sum += nums[i]
                if cur_sum >= s:
                    min_len = min(min_len, i - left + 1)
                    cur_sum -= nums[left]
                    left += 1
                    break

        return min_len
