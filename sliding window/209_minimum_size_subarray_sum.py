class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # [2,3,1,2,4,3] 7
        #. l
        #. r

        summation = 0
        min_len = len(nums) + 1
        l = 0
        
        for r in range(len(nums)):
            summation += nums[r]
            while summation >= target:
                min_len = min(min_len, r - l + 1)
                summation -= nums[l]
                l += 1

        return min_len if min_len != len(nums) + 1 else 0