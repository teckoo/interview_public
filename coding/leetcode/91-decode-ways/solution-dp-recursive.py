# https://leetcode.com/problems/decode-ways/solution/
class Solution:
    def __init__(self):
        self.memo = collections.defaultdict(int)

    def search(self, index: int, s: string) -> int:
        if not s: return 0
        if index == len(s): return 1  # this 1 is actually for previous token

        if s[index] == '0': return 0

        if index == len(s) - 1: return 1. ## '0' is handled above

        if index not in self.memo:
            ans = self.search(index + 1, s) + \
                    (self.search(index + 2, s) if (int(s[index:index+2])<=26) else 0)
            self.memo[index] = int(ans)

        return self.memo[index]

    def numDecodings(self, s: str) -> int:
        if not s or len(s) == 0: return 0
        return int(self.search(0, s))
