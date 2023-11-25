class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # [2,5,6,0,0,1,2]
        #           mid
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True

            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            elif nums[left] == nums[mid]:
                left += 1

        return False
    

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # [2,5,6,0,0,1,2,2]
        #          mid
        left = 0
        right = len(nums) - 1
 
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True

            if nums[left] < nums[mid]:
                if nums[mid] < target or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

            elif nums[left] > nums[mid]:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            elif nums[left] == nums[mid]:
                left += 1
        return False