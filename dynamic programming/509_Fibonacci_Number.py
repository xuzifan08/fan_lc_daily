class Solution:
    def fib(self, n: int) -> int:
        cache= {}

        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            if i == 2:
                return 1 + 0

            if i in cache:
                return cache[i]

            cache[i] = dp(i-1) + dp(i-2)

            return cache[i]

        return dp(n)