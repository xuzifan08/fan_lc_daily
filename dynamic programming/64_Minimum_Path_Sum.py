class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        res = [[float('inf')for i in range(cols+1)] for j in range(rows+1)]
        res[rows][cols - 1] = 0
        for r in range(rows-1, -1, -1):
            for c in range(cols -1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r+1][c],res[r][c+1])

        return res[0][0]
    

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp = [[0 for j in range(cols)] for i in range(rows)]
        dp[rows-1][cols-1] = grid[rows-1][cols-1]

        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                if r + 1 == rows and c + 1 < cols:
                    dp[r][c] = grid[r][c] + dp[r][c + 1]
                elif r + 1 < rows and c + 1 == cols:
                    dp[r][c] = grid[r][c] + dp[r + 1][c]
                elif r + 1 < rows and c + 1 < cols:
                    dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c+1])
        return dp[0][0]
    
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp = [[0 for c in range(cols)] for r in range(rows)]

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if r == rows - 1 and c == cols - 1:
                    dp[r][c] = grid[r][c]
                elif r == rows -1:
                    dp[r][c] = dp[r][c + 1] + grid[r][c]
                
                elif c == cols - 1:
                    dp[r][c] = dp[r+1][c] + grid[r][c]
                else:
                    dp[r][c] = grid[r][c] + min(dp[r+1][c], dp[r][c+1])

        return dp[0][0]
