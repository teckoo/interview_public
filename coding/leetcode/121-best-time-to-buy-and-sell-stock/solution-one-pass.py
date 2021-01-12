class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: 
            return 0        
        else:
            low = 99999 # represent minimum price so far
            profitmax = 0
            for price in prices:
                if price > low:
                    profitmax = max(profitmax, price - low)
                elif price < low:
                    low = price

        return profitmax