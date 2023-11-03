class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # calculate presum
        presum = [nums[0]]
        valid = 0

        for num in nums[1:]:
            presum.append(num + presum[-1])

        
        for i in range(0, len(nums)-1):
            left = presum[i]
            right = presum[-1] - presum[i]
            if left >= right:
                valid += 1
        
        return valid