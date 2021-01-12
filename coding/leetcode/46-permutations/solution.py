class Solution:
    def __init__(self):
        self.memo = collections.defaultdict(list)

    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        if len(nums) == 1: return [nums]
        if tuple(nums) not in self.memo:
            ans = []
            for i in range(len(nums)):
                ans.extend([[nums[i]] + r for r in self.permute(nums[:i] + nums[i+1:])])
            self.memo[tuple(nums)] = ans
        return self.memo[tuple(nums)]
