class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # maximum subarray with sum == sum(nums) - x
        summation = sum(nums) - x

        max_len = -1 
        cur_sum = 0
        left = 0
        
        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum > summation and left <= right:
                cur_sum -= nums[left]
                left += 1
            if cur_sum == summation:
                max_len = max(max_len, right - left + 1)
        
        return len(nums) - max_len if max_len!= -1 else -1