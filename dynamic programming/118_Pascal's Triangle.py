class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(1, numRows + 1):
            row = []

            for j in range(i):
                if j == 0 or j == i-1:
                    row.append(1)

                else:
                    row.append(res[-1][j-1] + res[-1][j])

            res.append(row)

        return res
    

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for row in range(1,numRows + 1):
            level = []
            for i in range(row):
                if i == 0 or i == row - 1:
                    level.append(1)
                else:
                    level.append(res[-1][i-1] + res[-1][i])
            res.append(level)

        return res