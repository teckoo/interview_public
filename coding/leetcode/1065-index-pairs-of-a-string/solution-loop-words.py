""" This solution loops words in text and find all positions. 
It needs to sort the result. 
But this one is faster.
"""
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []
        for word in words:
            i = text.find(word)
            while i != -1:
                res.append((i, i+len(word)-1))
                i = text.find(word, i+1)  # str.find(word, start, end)
        res.sort()
        return res
