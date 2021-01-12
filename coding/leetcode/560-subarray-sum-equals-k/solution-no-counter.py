# https://leetcode.com/problems/subarray-sum-equals-k/discuss/102111/Python-Simple-with-Explanation 
# first comment by lee215
# time: O(N)
import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        def subarraySum(self, nums, k):
            count, sum, res = {0: 1}, 0, 0
            for v in nums:
                sum += v
                res += count.get(sum - k, 0)
                count[sum] = count.get(sum, 0) + 1
            return res
