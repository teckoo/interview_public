class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dict_set = set()
        self.abbr_map = {}
        for word in dictionary:
            if word not in self.dict_set:
                self.dict_set.add(word)
                abbr = self.convert(word)
                self.abbr_map[abbr] = self.abbr_map.get(abbr, 0) + 1

    def convert(self, word):
        if not word: return 
        if len(word) < 3: 
            return word
        else:
            return "%s%d%s"%(word[0], len(word[1:-1]), word[-1])

    def isUnique(self, word: str) -> bool:
        abbr = self.convert(word)
        print(abbr)
        return abbr not in self.abbr_map or (word in self.dict_set and self.abbr_map.get(abbr, 0) == 1)


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
