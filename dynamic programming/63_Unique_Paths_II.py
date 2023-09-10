class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M,N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * N
        dp[N-1] = 1



        for r in reversed(range(M)):
            for c in reversed(range(N)):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c + 1 < N:
                    dp[c] = dp[c] + dp[c + 1]
        return dp[0]
    

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [0] * cols

        dp[-1] = 1


        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0

                elif c + 1 < cols:
                    dp[c] = dp[c] + dp[c+1]

        return dp[0]