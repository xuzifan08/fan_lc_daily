class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #  0 1 2 3 num = 5.5
        # [1,3,5,6]
        #.     l
        #.     r
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            num = nums[mid]

            if num == target:
                return mid

            elif num < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left 
                

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # [1,3,5,6] target = 2
        #. 0 1 2 3
        #. l
        #. r
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left
    

# this approach is the best to understand, in every condition, think about how to shrink the range to fulfill the insertion
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # [1,3,5,6] target = 2
        #. 0 1 2 3
        #. l
        #. r
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # right = mid because that in this case, we should insert at least starting from mid to 0 index
                right = mid
            elif nums[mid] < target:
                # right = mid because that in this case, we should insert at least starting from mid + 1 to max index
                left = mid + 1

        return left
    

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # [1,3,5,7] target = 6
        #. l.    l  
        #.       r

        left = 0
        right = len(nums)  

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                return mid

        return left
    

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # [1,3,5,7] target = 4
        #  0,1,2,3 
        #.     l     
        #.     r   
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid

        return left