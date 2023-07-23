class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [7,1,5,3,6,4]
        max_profit = 0
        min_price = max(prices)

        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit