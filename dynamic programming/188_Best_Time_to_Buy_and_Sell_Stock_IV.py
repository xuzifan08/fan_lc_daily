class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        cache = {}

        def dp(i, holding, remain):
            if i == len(prices) or remain ==0:
                cache[(i, holding, remain)] = 0
                return 0

            if (i, holding, remain) in cache:
                return cache[(i, holding, remain)]

            ans = dp(i + 1, holding, remain) # if we skip the transaction for the next day price

            # if we don't skip
            if holding:
                ans = max(ans, prices[i] + dp(i + 1, False, remain-1))
            else:
                ans = max(ans, -prices[i] + dp(i + 1, True, remain))
            cache[(i, holding, remain)] = ans

            return ans
        return dp(0, False, k)
    

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        cache = {}

        def dp(i, hold, remain):
            if i == len(prices) or remain == 0:
                return 0
            if (i, hold, remain) in cache:
                return cache[((i, hold, remain))]

            # skip the tranaction
            ans = dp(i + 1, hold, remain)
            if hold:
                ans = max(ans, prices[i] + dp(i+1, not hold, remain - 1))
            else:
                ans = max(ans, -prices[i] + dp(i+1, not hold, remain))

            cache[(i, hold, remain)] = ans
            return ans

        return dp(0, False, k)