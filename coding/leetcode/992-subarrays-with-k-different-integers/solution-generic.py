# https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/235002/One-code-template-to-solve-all-of-these-problems!
# 3. Longest Substring Without Repeating Characters:
# 992. Subarrays with K Different Integers:
# 159. Longest Substring with At Most Two Distinct Characters:
# 340. Longest Substring with At Most K Distinct Characters:
# 1248. Count Number of Nice Subarrays

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.subarraysWithAtMostKDistinct(A, K) - self.subarraysWithAtMostKDistinct(A, K-1)
    
    def subarraysWithAtMostKDistinct(self, s, k):
        lookup = collections.defaultdict(int)
        l, r, counter, res = 0, 0, 0, 0
        while r < len(s):
            lookup[s[r]] += 1
            if lookup[s[r]] == 1:
                counter += 1
            r += 1   
            while l < r and counter > k:
                lookup[s[l]] -= 1
                if lookup[s[l]] == 0:
                    counter -= 1
                l += 1
            res += r - l 
        return res
