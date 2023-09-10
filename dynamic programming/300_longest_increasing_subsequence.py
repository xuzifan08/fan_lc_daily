class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [10,9,2,5,3,7,101,18]
        # [1, 1,1,1,1,1,1,  1]
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
    


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)

        return max(lis)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #     [10,9,2,5,3,7,101,18]
        # dp. [1, 1,1,1,1,1, 1,  1]

        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)


        return max(dp)
       