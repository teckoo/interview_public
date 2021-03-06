# Trie Template

[Explaination Details](./summary.md) | [Template Index](../template_list.md)

* Time complexity: O(L) insert, update
* Space complexity: O(N*L), N: number of words, L: word length.

```python
"""
Implement Trie in default dict to save space

LC 1065 shows a smart solution to work on TrieNode directly to search a string.
${leetcode}/problem/1065-index-pairs-of-a-string
"""


class TrieNode:
    """ structure of a TrieNode """

    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    """ basic operation of a Trie """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """ insert a key in a trie """
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_word = True

    def search(self, key):
        """ search whether a word is in a trie """
        if key is None:
            return False
        node = self.root
        for char in key:
            node = node.children.get(char, None)
            if node is None:
                return False
            if node.is_word:
                return True
        return False

    def build_words(self, words):
        """ initialize a list of words to a trie """
        for word in words:
            self.insert(word)

    def count(self):
        """ return number of words in a trie """

        def _count(root):
            if root is None:
                return 0
            result = 1 if root.is_word else 0
            result += sum(_count(child) for child in root.children.values())
            return result

        return _count(self.root)

    def list(self):
        """ return all words in a trie """
        result = []

        def find_word(node, prefix, char):
            if node is None:
                return
            if node.is_word:
                result.append(prefix + char)
            for key, child in node.children.items():
                find_word(child, prefix + char, key)

        find_word(self.root, "", "")
        return result


keys = ["the", "a", "there", "answer", "any",
        "by", "bye", "their", "abc"]

t = Trie()
print("Keys to insert: ")
print(keys)

t.build_words(keys)
print(t.count())
print(sorted(t.list()))  # based on list(), we can sort the result.
```