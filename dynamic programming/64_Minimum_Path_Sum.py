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