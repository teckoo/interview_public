class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0: return 0
        lo = hi = prices[0]
        profit = 0
        for price in prices[1:]:
            if price >= hi:  # hold
                hi = price
            elif price < hi:  # take profit
                profit += hi - lo
                # print(f"lo={lo}, hi={hi}, {hi-lo}, profit={profit}")
                lo = hi = price
        return profit + ((hi - lo) if hi > lo else 0)
