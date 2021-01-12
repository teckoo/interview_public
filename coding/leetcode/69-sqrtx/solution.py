"""
Runtime: 32 ms, faster than 91.71% of Python3 online submissions for Sqrt(x).
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Sqrt(x).
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1: return x
        
        lb, ub = 1, x
        while lb < ub:
            m = lb + (ub - lb) // 2
            # print(f"{lb}, {m}, {ub}")
            
            if m * m <= x and (m+1)*(m+1) > x: 
                return m
            elif m * m < x:
                lb = m + 1
            else: 
                ub = m - 1
        return ub 
