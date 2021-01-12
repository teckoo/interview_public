# answer_without_carry is a ^ b
# carry bit is (a & b) << 1
# e.g  in python XOR is `^`
# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 1 = 0
# find carry bit
# 0 & 0 = 0
# 0 & 1 = 1
# 1 & 1 = 0  
# NOTE: # (1 & 1)<<1 == 2 carry bit moves to the next bit
class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]
