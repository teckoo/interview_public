class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        0:1 ""
        1:1 (f0)
        2:2 (f0)f1, (f1)) - "()()", "(())"
        3:5 (f0)f2, (f1)f1, (f2)f0
        4:14
        closure number is sort of DP: for each N, it adds "()" to each left,
        then right part (N - 1 - left).
        """
        if n == 0: return [""]
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - 1 - c):
                    ans.append('({}){}'.format(left, right))
        return ans
