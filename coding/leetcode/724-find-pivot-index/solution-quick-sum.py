class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (total - leftsum - x):
                return i
            leftsum += x
        return -1
