# Runtime: 44 ms, faster than 97.38% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Substring Without Repeating Characters.


# Approach 3: Sliding Window Optimized

class Solution:
    def lengthOfLongestSubstring(self, s):
        dicts = {}
        maxlength = start = 0
        for i,value in enumerate(s):
            if value in dicts:
                sums = dicts[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            dicts[value] = i
        return maxlength
