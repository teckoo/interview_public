from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = Counter(s)
        for ch in t:
            counter[ch] -= 1
        return not any(counter.values())
