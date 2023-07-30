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
    


class Solution:
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    # [2,3,1,2,4,3]
    #  l
    #. r
    left = 0
    curr_val = 0
    size = len(nums) + 1

    for right in range(len(nums)):
        curr_val += nums[right]

        while curr_val >= target:
            size = min(size, right - left + 1)
            curr_val -= nums[left]
            left += 1
            

    return size if size != len(nums) + 1 else 0
    

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # [2,3,1,2,4,3]
        #  l
        #. r
        
        left = 0 
        res = len(nums) + 1
        summation = 0

        for right in range(len(nums)):
            summation += nums[right]

            while summation >= target:
                res = min(res, right - left + 1)
                summation -= nums[left]
                left += 1

        return res if res != len(nums) + 1 else 0

