class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jems = set(J)
        return sum(1 for s in S if s in jems)
