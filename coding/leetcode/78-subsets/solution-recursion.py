class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        output = [[]]  # this is a trick

        for n in nums:
            output += [cur + [num] for cur in output]
        return output
