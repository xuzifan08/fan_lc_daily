class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
  #.    l.    r
#     [[1, 2, 3 ,4],
 # tb  [5, 6, 7, 8],
 #     [9,10,11,12]]
        left = 0
        right = len(matrix[0])-1

        top = 0
        bottom = len(matrix)-1
        direction = 0

        res = []

        while left <= right and top <= bottom:
            if direction == 0:
                i = left
                while i <= right:
                    res.append(matrix[top][i])
                    i += 1
                top += 1
            elif direction == 1:
                i = top
                while i <= bottom:
                    res.append(matrix[i][right])
                    i += 1
                right -=1
            elif direction == 2:
                i = right
                while i >= left:
                    res.append(matrix[bottom][i])
                    i -= 1
                bottom -= 1
            else:
                i = bottom
                while i >= top:
                    res.append(matrix[bottom][left])
                    i -= 1
                left += 1
            direction += 1
            direction = direction % 4

        return res


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # [[1,2,3,4],
        #  [5,6,7,8],
        #  [9,10,11,12]] 
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        direction = 0
        res = []

        while top <= bottom and left <= right:
            if direction == 0:
                i = left
                while i <= right:
                    res.append(matrix[top][i])
                    i += 1
                top += 1
            elif direction == 1:
                i = top
                while i <= bottom:
                    res.append(matrix[i][right])
                    i += 1
                right -=1

            elif direction == 2:
                i = right
                while i >=left:
                    res.append(matrix[bottom][i])
                    i -= 1
                bottom -= 1
            else:
                i = bottom
                while i >= top:
                    res.append(matrix[i][left])
                    i -= 1
                left += 1
            direction += 1
            direction = direction % 4

        return res