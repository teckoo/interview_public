""" This solution loops text to find all combinations in words. 
The result will be sorted natually. 
"""
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        result = []
        words = set(words)
        for i in range(len(text)):
            for j in range(1, len(text)+1):
                if text[i:j] in words:
                    result.append([i, j-1])
        return result
