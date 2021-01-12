# Runtime: 24 ms, faster than 94.78% of Python3 online submissions for First Bad Version.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for First Bad Version.
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 0, n
        while lo < hi: 
            m = lo + (hi - lo) // 2
            if isBadVersion(m):
                hi = m
            else:
                lo = m + 1
        return lo
