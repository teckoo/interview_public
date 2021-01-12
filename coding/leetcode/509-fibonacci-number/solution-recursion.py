class Solution:
    def __init__(self):
        self.mem = {0: 0, 1: 1}

    def fib(self, N: int) -> int:
        if N in self.mem: return self.mem[N]

        result = self.fib(N - 1) + self.fib(N - 2)
        self.mem[N] = result
        return result
