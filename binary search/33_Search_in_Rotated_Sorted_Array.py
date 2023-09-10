class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [4,5,6,7,0,1,2] target = 0
        #. 0,1,2,3,4,5,6
        #. l     m     r
        # [6,7,0,1,2,3,4] target = 3

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target: return mid

            if nums[mid] >= nums[0]:
                if target > nums[mid] or target < nums[0]:
                    left = mid + 1

                else:
                    right = mid - 1

            else:
                if target < nums[mid] or target > nums[-1]:
                    right = mid - 1
                else:
                    left = mid + 1


        return -1 
