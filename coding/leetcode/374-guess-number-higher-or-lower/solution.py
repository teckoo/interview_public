# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            m = l + (r-l)//2
            result = guess(m)
            # print(f"{m}, {result}")
            if result == 1:
                l = m + 1
            elif result == -1:
                r = m - 1
            else:  # found it
                return m
        return -1