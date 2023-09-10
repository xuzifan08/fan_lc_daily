class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # [5,7,7,8,8,8,10]
        #.     l   m   r
        left = 0 
        right = len(nums) - 1

        while left <= right:
            if nums[left] == nums[right] == target:
                return [left, right]
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

            elif nums[mid] == target:
                if nums[left] == target:
                    right -= 1
                elif nums[right] == target:
                    left += 1
                else:
                    right -= 1
                    left += 1
        return [-1, -1]