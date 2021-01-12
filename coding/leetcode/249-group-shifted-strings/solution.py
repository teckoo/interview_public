class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        word_grp = {}
        for word in strings:
            key_list = []
            for i in range(len(word) - 1):
                key = (ord(word[i+1]) - ord(word[i])) % 26
                key_list.append(key)
            tuple_key = tuple(key_list)
            print(f"{word}: {tuple_key}")
            word_grp.setdefault(tuple_key, []).append(word)
        return word_grp.values()
