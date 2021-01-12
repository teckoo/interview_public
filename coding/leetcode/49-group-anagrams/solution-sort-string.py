# Note that dict, set and list are not hashable,
# but *tuple* can be a hash key.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            key = tuple(sorted(word))
            # print(word, key)
            group.setdefault(key, []).append(word)
        
        return group.values()