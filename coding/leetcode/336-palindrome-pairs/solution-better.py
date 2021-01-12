class Solution:
    def palindromePairs(self, words):
        def isPalindrome(word):
            return word == word[::-1]
        output = []
        word_to_index = {word: i for i, word in enumerate(words)}
        for i, word1 in enumerate(words):
            for j in range(len(word1)+1):
                # Case 1 - Find all words, B, shorter than or the same size as
                # word1, that can be prepended so B + word1 is a palindrome.
                x_reversed = word1[j:][::-1]
                rest = word1[0:j]
                if isPalindrome(rest) and x_reversed in word_to_index and word_to_index[x_reversed] != i:
                    output.append([word_to_index[x_reversed], i])
                # Case 2 - Find all words, B, shorter than word1 that can be appended
                # so word1 + B is a palindrome.
                if j == len(word1): continue
                x_reversed = word1[:j][::-1] 
                rest = word1[j:]
                if isPalindrome(rest) and x_reversed in word_to_index and word_to_index[x_reversed] != i:
                    output.append([i, word_to_index[x_reversed]])
        return output
