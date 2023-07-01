from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1

        def valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 0

        n = len(grid)
        queue = deque([(0,0,1)])
        seen = {(0,0)}
        directions = [(0, 1), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1), (0, -1), (-1, 0)]

        while queue:
            
            row, col, steps = queue.popleft()

            if (row, col) == (n-1, n-1):
                return steps

            for r, c in directions:
                new_row = r + row
                new_col = c + col
                if valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    queue.append((new_row, new_col, steps + 1))
        return -1