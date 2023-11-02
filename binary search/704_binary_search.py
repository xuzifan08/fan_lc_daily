class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1

        return -1
    

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if you want to return in while loop, include "=" in the condition
        
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right+1) // 2
            print(left, right, mid, nums[mid], target)

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
    

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if you want to return in while loop, include "=" in the condition
        left = 0
        right = len(nums) - 1
        # [-1,0,3,5,9,12]
        #.  0,1,2,3,4,5

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
    

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [-1,0,3,5,9,12] 9
        #.  l.  m lr
        left = 0 
        right = len(nums) - 1

        while left < right:
            mid = (left + right)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                return mid

        return left if nums[left] == target else -1