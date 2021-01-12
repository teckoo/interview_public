class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1.0

        if n < 0: return 1 / self.myPow(x, -n)  # convert to positive n
        ans = 1
        while n:
            if n & 1:  # equivlent to n % 2
                ans *= x
            x *= x
            n = n >> 1  # equals to n /= 2
        return ans
