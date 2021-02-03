class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(n):
            """ get N from subproblems """
            # check result
            if n in memo: return memo[n]
            # base
            if n == 0: return 0
            if n < 0: return -1
            
            # solve sub problems
            res = float("inf")
            for coin in coins:
                sub_res = dp(n - coin)
                if sub_res == -1: continue
                res = min(res, sub_res + 1)
            # save result to memo
            memo[n] = res if res != float("inf") else -1
            return memo[n] 
        return dp(amount)
