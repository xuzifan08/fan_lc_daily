class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        # [4,5,6,7,0,1,2] 
        #.         l r 

        # [3,4,5,1,2]
        #  l.    l r
        left = 0 
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid

        return nums[left]
