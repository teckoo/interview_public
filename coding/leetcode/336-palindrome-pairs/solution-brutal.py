class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(one: str, two: str) -> bool:
            return one+two == (one+two)[::-1]

        result = []
        for i, first in enumerate(words):
            for j, second in enumerate(words):
                if is_palindrome(first, second) and i!=j:
                    result.append([i, j])
        return result
