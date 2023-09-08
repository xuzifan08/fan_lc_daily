class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        # figure out the a funtion with a state and what it returns
        def dp(i): # index of the array
            if i == 0:
                memo[i] = 0

            if i == 1:
                memo[i] = 0


            # the base case
            if i in memo:
                return memo[i]

            # figure out the transition between different state
            memo[i] = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])

            return memo[i]# min cost to get to this point

        return dp(len(cost))