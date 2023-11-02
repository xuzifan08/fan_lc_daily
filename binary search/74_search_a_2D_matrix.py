class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        left = 0
        right = rows * cols -1

        while left <= right:
            mid = (left + right) // 2
            
            r = mid // cols
            c = mid % cols
            print(r, c, mid)

            num = matrix[r][c]

            if num == target:
                return True
            elif target > num:
                left = mid + 1
            else:
                right = mid - 1
        print(14//3)

        return False
    

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols - 1


        while left <= right:
            mid = (left + right) // 2
            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False