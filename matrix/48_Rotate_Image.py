class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix) - 1

        while l < r:
            top = l
            bottom = r
            
            for i in range(r - l):
                temp = matrix[top][l + i]
                matrix[top][l+i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top+i][r]
                matrix[top+i][r] = temp

            l += 1
            r -= 1