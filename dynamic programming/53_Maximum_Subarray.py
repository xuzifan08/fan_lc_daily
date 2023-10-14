class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_subarray = nums[0]
        max_subarray = nums[0]

        for num in nums[1:]:
            curr_subarray = max(num, curr_subarray + num)
            max_subarray = max(curr_subarray, max_subarray)

        return max_subarray