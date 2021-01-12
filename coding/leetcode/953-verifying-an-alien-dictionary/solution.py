class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        map_s = {c:i for i, c in enumerate(order)}

        def compare(word):
            t = []
            for c in word:
                t.append(map_s[c])
            return tuple(t)

        return words == sorted(words, key = compare)
