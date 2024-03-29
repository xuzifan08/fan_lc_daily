class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # return the longest subarray with no more than k 0s
        zero = 0
        left = 0
        longest = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero += 1

            while zero > k:
                if nums[left] == 0:
                    zero -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest