class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1

            else:
                right = mid

        return right
    

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        # [1,2,1,3,5,6,4]
        #  0,1,2,3,4,5,6
        #.         l   r
        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            elif nums[mid] > nums[mid + 1]:
                right = mid

        return left
    
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        # [1,2,1,3,5,6,4]
        #  0,1,2,3,4,5,6
        #.         l   r
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            elif nums[mid] > nums[mid + 1]:
                right = mid

        return left