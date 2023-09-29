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
    

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1
        # nums = [0,1,2,2,3,0,4,2,2], val = 2
        length = len(nums) - 1
        right  = length
        left = 0
        # [3,3]
        #    l
        #  r


        while left < right:
            if nums[right] == val:
                right -= 1
            else:
                if nums[left] == val:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
                else:
                    left += 1

        return left + 1 if nums[left]!= val else left
