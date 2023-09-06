class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        # print(board)
        board.reverse()
        # print(board)
        # reverse the board to make sure the conversion from int to rows/columns easier
        def int_to_pos(square):
            r = (square - 1) // length
            c = (square - 1) % length

            if r % 2:
                c = length - 1 - c
            return [r, c]

        # use a helper function to convert int to row/column

        # use BFS to count the moves
        queue = collections.deque([(1, 0)])
        visited = set()

        while queue:
            square, moves = queue.popleft()

            for i in range(1, 7):
                next_square = square + i
                r, c = int_to_pos(next_square)

                if board[r][c]!= -1:
                    next_square = board[r][c]
                if next_square == length * length:
                    return moves + 1

                if next_square not in visited:
                    visited.add(next_square)
                    queue.append([next_square, moves+1])

        return -1