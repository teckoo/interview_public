class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s and not t: return True
        if not s or not t or len(s) != len(t): return False

        map_s = {}
        map_t = {}
        size = len(s)
        for i in range(size):
            cs, ct = s[i], t[i]
            if cs in map_s:
                if map_s.get(cs) != ct:
                    return False
            if ct in map_t:
                if map_t.get(ct) != cs:
                    return False
            map_s[cs] = ct
            map_t[ct] = cs
        return True
