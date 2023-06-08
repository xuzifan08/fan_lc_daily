class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # use [row][col] to represent a node
        # iterate through row col, every time search for four directions, if it's a ground, add to seen and keep searching

        seen = set()
        islands = 0

        def valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "1"

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row, col):
            for a, b in directions:
                next_row = row + a
                next_col = col + b
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    dfs(next_row, next_col)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in seen:
                    islands += 1
                    seen.add((row, col))
                    dfs(row, col)

        return islands