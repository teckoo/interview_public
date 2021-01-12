class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        write = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[write] = nums[i]
                write += 1
        return write
