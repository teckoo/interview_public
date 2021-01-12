class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        1:1 ()
        2:2 ()(), (())
        3:5
        4:14
        backtracking, enumerate adding "(" to each position until it reaches 2*N length.
        """
        ans = []
        def backtrack(s = '', left = 0, right = 0):
            if len(s) == 2 * n:  # done
                ans.append(s)
                return

            if left < n:
                backtrack(s + "(", left + 1, right)
            if right < left:
                backtrack(s + ")", left, right + 1)

        backtrack()
        return ans

