class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []

        for i in range(2**n, 2**(n+1)):
            # generate bitmask from 000 to 111
            bitmask = bin(i)[3:]  # skip '0b1', get the last 3 bits

            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j]=='1'])

        return output
