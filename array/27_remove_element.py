class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1:
            return 1 if nums[0] != val else 0
        # nums = [3,2,2,3], val = 3
        # [2,2,3,3]
        left = 0
        right = len(nums) - 1
        num = 0

        while left < right:
            num += 1

            if nums[right] != val:
                if nums[left] == val:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
                else:
                    left += 1
            else:
                right -= 1
            
        return left + 1 if nums[left] != val else left