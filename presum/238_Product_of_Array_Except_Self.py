class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,3,4]
        # [1,1,2,6] pre_product
        # [24,12,4,1]

        pre_product = [1] * len(nums)

        for i in range(1, len(nums)):
            pre_product[i] = pre_product[i-1] * nums[i-1]

        post_product = [1] * len(nums)

        for j in range(len(nums)-2, -1,-1):
            post_product[j] = post_product[j+1] * nums[j+1]

        res = [0] * len(nums)


        for i in range(len(nums)):
            res[i] = pre_product[i] * post_product[i]

        return res
    

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,3,4]
        # [1,1,2,6] pre_product
        # [24,12,4,1]
        pre_product = [1] * len(nums)
        post_product = [1] * len(nums)

        for i in range(1, len(nums)):
            pre_product[i] = pre_product[i - 1] * nums[i-1]

        for j in range(len(nums)-2, -1, -1):
            post_product[j] = post_product[j+1] * nums[j+1]


        output = []

        for k in range(len(nums)):
            output.append(pre_product[k]*post_product[k])

        return output