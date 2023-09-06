class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # capture all the unsurrounded regions
        rows  = len(board)
        cols = len(board[0])

        def dfs(r, c):
            if  r < 0 or c < 0 or r == rows or c == cols or board[r][c]!= "O":
                return
            # print(r, c)
            board[r][c] = "T"
            # print(board)
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols - 1]):
                    dfs(r,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                elif board[r][c]=="T":
                    board[r][c]="O"