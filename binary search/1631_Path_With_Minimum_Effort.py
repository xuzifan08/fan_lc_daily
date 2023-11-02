class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        def valid(r, c):
            return 0<=r<len(heights) and 0<=c<len(heights[0])

        def check(effort):
            seen = {(0,0)}
            stack = []
            stack.append((0,0))
            directions = [[0,1],[0,-1],[1,0],[-1,0]]

            while stack:
                r, c = stack.pop()

                if r == len(heights)-1 and c==len(heights[0])-1:
                    return True
                
                for dir_r, dir_c in directions:
                    next_r = r+dir_r
                    next_c = c+dir_c
                    if valid(next_r, next_c) and (next_r,next_c) not in seen:
                        if abs(heights[next_r][next_c] - heights[r][c]) <= effort:
                            seen.add((next_r, next_c))
                            stack.append((next_r, next_c))

            return False
        

        left = 0
        right = max(max(row) for row in heights)

        while left < right:
            mid = (left + right) // 2
            finish = check(mid)

            if finish:
                right = mid
            elif not finish:
                left = mid + 1

        return right