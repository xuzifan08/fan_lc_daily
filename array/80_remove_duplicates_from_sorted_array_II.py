class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [0,0,0,1,1,1,2,3,3]
        #  l
        #      r
        # count = 3
        l, r = 0, 0

        while r < len(nums):
            count = 1

            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                count += 1
                r += 1
            
            for i in range(min(count, 2)):
                nums[l] = nums[r]
                l += 1
            r += 1
        
        return l