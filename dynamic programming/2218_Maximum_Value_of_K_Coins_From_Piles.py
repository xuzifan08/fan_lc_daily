class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [[-1] * (k + 1) for _ in range(len(piles))] 

        def dpdp(i, coins):
            if i == len(piles):
                return 0
            if dp[i][coins] != -1:
                return dp[i][coins]

            # skip this pile
            dp[i][coins] = dpdp(i + 1, coins)
            curr = 0
            for j in range(min(coins, len(piles[i]))):
                curr += piles[i][j]
                dp[i][coins] = max(dp[i][coins], curr + dpdp(i + 1, coins -j- 1))
            
            return dp[i][coins]

        return dpdp(0, k)