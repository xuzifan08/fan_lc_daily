class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # [0,1,1,1,0,1,1,0,1]
        left = 0
        zero = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero += 1
            while zero > 1:
                if nums[left] == 0:
                    zero -= 1
                left += 1
            
            max_len = max(max_len, right - left)

        return max_len
    
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # [0,1,1,1,0,1,1,0,1]
        #. l
        #. r
        delete = 0
        longest = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                delete += 1

            while delete > 1:
                if nums[left] == 0:
                    delete -= 1
                left += 1
            longest = max(longest, right - left + 1)

        return longest - 1
