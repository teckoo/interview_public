# Runtime: 108 ms, faster than 23.72% of Python3 online submissions for Word Break II.
# Memory Usage: 13.2 MB, less than 86.21% of Python3 online submissions for Word Break II.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {len(s): ['']}
        def sentences(i):
            """
            sentences(i) returns a list of all sentences that 
            can be built from the suffix s[i:].
            """
            if i not in memo:
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                           for j in range(i+1, len(s)+1)
                           if s[i:j] in wordDict
                           for tail in sentences(j)]
            return memo[i]
        return sentences(0)
