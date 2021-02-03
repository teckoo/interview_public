class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # plus base, make array as `size + 1`
        dp = [float("inf")] * (amount + 1)
        # base case
        dp[0] = 0
        # iterate all states
        for i in range(len(dp)):
            # go over each choice
            for coin in coins:
                # skip invalid sub problem
                if (i - coin) < 0: continue
                # check optimal sub-problem   
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1