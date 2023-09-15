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
    

from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1

        n = len(grid)
        queue = deque([(0,0,1)])
        directions = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]

        def valid(r, c):
            return 0 <= r < n and 0 <= c < n and grid[r][c] == 0

        visited = set()
        while queue:
            r, c, steps = queue.popleft()

            if (r, c) == (n-1, n-1):
                return steps

            for step_r, step_c in directions:
                next_r = r + step_r
                next_c = c + step_c

                if valid(next_r, next_c) and (next_r, next_c) not in visited:
                    queue.append((next_r, next_c, steps + 1))
                    visited.add((next_r, next_c))

        return -1
    

from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1


        def valid(r, c):
            return 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c]== 0
        
        visited = set()
        queue = collections.deque([(0,0,1)])

        directions = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]

        while queue:
            r, c, paths = queue.popleft()

            if (r, c) == (len(grid)-1, len(grid)-1):
                return paths

            for dir_r, dir_c in directions:
                next_r = r + dir_r
                next_c = c + dir_c

                if valid(next_r, next_c) and (next_r, next_c) not in visited:
                    queue.append((next_r, next_c, paths + 1))
                    visited.add((next_r, next_c))

        return -1