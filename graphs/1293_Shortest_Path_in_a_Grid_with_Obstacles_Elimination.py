class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if grid[0][0] == 1:
            k -= 1

        rows = len(grid)
        cols = len(grid[0])

        queue = collections.deque([(0,0,k,0)]) #(row, col, obstacles, steps)
        seen = {(0,0,k)}

        def valid(r, c):
            return 0 <=r<rows and 0<=c<cols

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            r, c, obs, steps = queue.popleft()
            if r == rows - 1 and c == cols -1:
                return steps
            
            for dir_r, dir_c in directions:
                next_r = dir_r + r
                next_c = dir_c + c

                if valid(next_r, next_c):
                    if grid[next_r][next_c] == 0 and (next_r, next_c, obs) not in seen:
                        seen.add((next_r, next_c, obs))
                        queue.append((next_r, next_c, obs, steps + 1))

                    elif grid[next_r][next_c] == 1 and obs - 1 >= 0 and (next_r, next_c, obs-1) not in seen:
                        seen.add((next_r, next_c, obs - 1))
                        queue.append((next_r, next_c, obs - 1, steps + 1))

        return -1
