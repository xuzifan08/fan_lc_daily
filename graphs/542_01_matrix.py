class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        queue = collections.deque()
        seen = set()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c, 0))
                    seen.add((r,c))


        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def valid(r,c):
            return 0<=r<rows and 0<=c<cols

        while queue:
            r, c, steps = queue.popleft()
            if mat[r][c] == 1:
                mat[r][c]= steps

            for dir_r, dir_c in directions:
                next_r = dir_r + r
                next_c = dir_c + c
                if valid(next_r, next_c) and (next_r, next_c) not in seen:
                    print(next_r, next_c)
                    queue.append((next_r, next_c, steps + 1))
                    seen.add((next_r, next_c))

        return mat
    