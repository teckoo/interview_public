"""
167: 

Runtime: 60 ms, faster than 96.58% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Two Sum II - Input array is sorted.
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1
        # if hi < 1: return [-1, -1]

        while lo < hi:
            cal = numbers[lo] + numbers[hi]
            if cal == target:
                return [lo+1, hi+1]
            elif cal < target:
                lo += 1
            else:
                hi -= 1
        return [-1, -1]
