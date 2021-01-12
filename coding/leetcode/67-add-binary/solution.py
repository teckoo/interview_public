class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        result = []
        carry = 0    
        for i in range(n-1, -1, -1): 
            carry, digit = divmod(sum([int(a[i]), int(b[i]), carry]), 2)
            result.append(str(digit))

        if carry:
            result.append(str(carry))

        return "".join(result[::-1])
