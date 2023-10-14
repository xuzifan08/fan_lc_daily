class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 10**9 + 7
        cache = {}

        def dp(n, p, i):
            # n - number of members left
            # p - profit so far
            # i - index so far

            # base cases
            if i == len(group):
                return 1 if p >= minProfit else 0

            if (n, p, i) in cache:
                return cache[(n, p, i)]

            cache[(n, p, i)] = dp(n, p, i + 1)

            if n - group[i] >= 0:
                cache[(n, p, i)] += dp(n - group[i], p + profit[i],i + 1)

            return cache[(n, p, i)] % mod

        return dp(n, 0, 0)