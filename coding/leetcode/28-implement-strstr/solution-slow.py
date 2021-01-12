class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        if l == 0: return 0
        for start in range(len(haystack)):
            if haystack[start:start+l] == needle: return start

        return -1
