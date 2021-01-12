# Runtime: 24 ms, faster than 83.32% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Climbing Stairs.
class Solution:
    def climbStairs(self, n: int) -> int:
        """ Give n will be a positive integer
        It's simply Fibonacci series
        """
        if n < 4: return n
        step_1 = 2  # n-2
        step_2 = 3  # n-1
        step = 0
        for _ in range(4, n+1):
            step = step_1 + step_2
            step_1 = step_2
            step_2 = step
        return step
