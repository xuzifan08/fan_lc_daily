class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}
        def dp(i):
            if i == 1:
                memo[1] = 1
                return memo[1]

            if i == 2:
                memo[2] = 2
                return memo[2]

            if i in memo:
                return memo[i]

            memo[i] = dp(i-1) + dp(i-2)

            return memo[i]

        return dp(n)
    

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(i):
            if i == 1:
                memo[1] = 1
                return 1
            if i == 2:
                memo[2] = 2
                return 2

            if i in memo:
                return memo[i]

            memo[i] = dp(i-1) + dp(i-2)
            return memo[i]

        return dp(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 -> n
        memo = {}
        def dp(i):
            if i == 1:
                memo[i] = 1
                return memo[i]
            if i == 2:
                memo[i] = 2
                return memo[i]
            # transition
            if i == 3:
                memo[i] = 3
                return memo[i]
            if i in memo:
                return memo[i]
            memo[i] = dp(i - 1) + dp(i - 2)

            return memo[i]

        return dp(n)
    

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(i):
            if i == 1:
                memo[i] = 1
                return memo[i]
            if i == 2:
                memo[i] = 2
                return memo[i]
            if i in memo:
                return memo[i]

            memo[i] = dp(i -1) + dp(i-2)

            return memo[i]

        return dp(n)


class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                cache[i] = 1
                return 1
            if i == 2:
                cache[i] = 2
                return 2
            if i in cache:
                return cache[i]
            cache[i] = dp(i-1) + dp(i-2)

            return cache[i]

        return dp(n)
    


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(n):
            if n == 0:
                memo[0] = 0
                return 0

            if n == 1:
                memo[1] = 1
                return 1

            if n == 2:
                memo[2] = 2
                return 2

            if n in memo:
                return memo[n]

            memo[n] = dp(n-1) + dp(n-2)
            return memo[n]

        return dp(n)