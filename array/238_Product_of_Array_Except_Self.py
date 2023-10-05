class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * postfix
            postfix *= nums[i]
        
        return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,3,4]
        # [1,1,2,6] pre_product
        # [24,12,4,1]
        res = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1

        for j in range(len(nums) - 1, -1, -1):
            res[j] = res[j] * postfix
            postfix = postfix * nums[j]

        return res