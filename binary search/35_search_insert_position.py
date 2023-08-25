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