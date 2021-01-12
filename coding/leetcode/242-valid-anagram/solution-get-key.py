from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def get_key(word):
            counter = Counter(word)
            key = [ch+str(counter[ch]) for ch in sorted(counter)]
            return "".join(key)

        return get_key(s) == get_key(t)
