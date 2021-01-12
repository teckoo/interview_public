class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0: return 0
        lo = hi = prices[0]
        ans = 0
        for price in prices[1:]:
            hi = max(hi, price)
            if price < lo:  # find a new low, check profit
                ans = max(ans, hi - lo)
                lo = hi = price
        return max(ans, hi - lo)
