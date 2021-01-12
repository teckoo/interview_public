# Runtime: 40 ms, faster than 18.55% of Python3 online submissions for Most Common Word.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Most Common Word.
from collections import defaultdict
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = defaultdict(int)
        max_word = 0
        word = None
        for w in re.split(" |!|\?|'|,|;|\.", paragraph):
            w = w.lower().replace('.','').replace('!','')\
                .replace('?','').replace(',','').replace("'",'').replace(';','')
            if len(w) > 0 and w not in banned:
                words[w] += 1
                if words[w] > max_word:
                    max_word = words[w]
                    word = w
        return word
