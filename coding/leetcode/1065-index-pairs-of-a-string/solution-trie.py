class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        # n - len(text)
        # m - sum(len(word))

        # build words trie - O(m)
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.is_word = False

        root = TrieNode()

        for word in words:
            node = root
            for char in word:
                node = node.children.setdefault(char, TrieNode())
            node.is_word = True

        # scan text for words - O(n*max_word_len) <= O(n*m)
        output = []
        for i in range(len(text)):
            node = root
            for j in range(i, len(text)):
                char = text[j]
                node = node.children.get(char, None)
                if node is None:
                    break
                if node.is_word:
                    output.append([i,j])
        return output
