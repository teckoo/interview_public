class Solution:
    def __init__(self):
        self.mem = {}

    def climbStairs(self, n: int) -> int:
        """ Give n will be a positive integer
        It's simply Fibonacci series
        """
        if n < 4: return n

        # current step depends on previous two stairs
        if n not in self.mem:
            res =  self.climbStairs(n - 2) + self.climbStairs(n - 1)
            self.mem[n] = res
        return self.mem[n]
