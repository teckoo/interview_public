class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s: return s
        stack = []  # for left parentheses
        bad_right = 0
        ans = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i - bad_right)
            elif c== ')':
                if stack:
                    stack.pop()
                else: # invalid ), skip
                    bad_right += 1
                    continue
            ans.append(c)
#        print(f"{stack}")            
        while stack:
            i = stack.pop()
            del ans[i]
        return "".join(ans)
