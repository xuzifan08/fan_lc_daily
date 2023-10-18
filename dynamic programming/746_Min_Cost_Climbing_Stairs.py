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
    

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dp(i):
            # base case
            if i == 0:
                memo[i] = 0
                return 0

            if i == 1:
                memo[i] = 0
                return 0

            if i in memo:
                return memo[i]

            memo[i] = min(dp(i - 1) + cost[i-1], dp(i-2) + cost[i-2])

            return memo[i]# min cost to climb to i
        return dp(len(cost))
    



class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        # [1,100,1,1,1,100,1,1,100,1]
        def dp(i):
            if i == 0:
                memo[i] = 0
                return 0
            if i == 1:
                memo[i] = 0
                return memo[i]
            if i == 2:
                memo[i] = min(cost[0], cost[1])   
            if i in memo:
                return memo[i]            

            memo[i] = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])

            return memo[i]

        return dp(len(cost))
