class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m-1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow

        return row[0]
    


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m)]

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r == m -1 or c == n -1:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r+1][c] + dp[r][c+1]

        return dp[0][0]