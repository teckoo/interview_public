# Runtime: 4624 ms, faster than 27.02% of Python3 online submissions
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for 
# Longest Palindromic Substring.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        len_ans = 0
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len_ans >= j-i:
                    break
                if s[i:j] == s[i:j][::-1]:
                    ans = s[i:j]
                    len_ans = len(ans)
        return ans
