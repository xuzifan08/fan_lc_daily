class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_subarray = nums[0]
        max_subarray = nums[0]

        for num in nums[1:]:
            curr_subarray = max(num, curr_subarray + num)
            max_subarray = max(curr_subarray, max_subarray)

        return max_subarray
    
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # [-2,1,-3,4,-1,2,1,-5,4]
        largest_sum = float('-inf')
        curr_sum = 0
        
        for num in nums:
            curr_sum = max(curr_sum + num, num)
            largest_sum = max(largest_sum, curr_sum)

        return largest_sum
