class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0: return ""
        for i, c in enumerate(strs[0]):
            for s in strs:
                # print(f"c = {c}, s[i]={s[i]}")
                if i >= len(s) or s[i]!=c: 
                    return strs[0][:i]
        return strs[0]
