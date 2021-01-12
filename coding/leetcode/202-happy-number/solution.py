class Solution:
    def isHappy(self, n: int) -> bool:
        def convert(n) -> int:
            digits = [int(c) for c in str(n)]
            return sum(d*d for d in digits)

        memo = set()
        item = n
        while True:
            if item in memo:
                return False
            else:
                memo.add(item)
            if item == 1: return True
            item = convert(item)
