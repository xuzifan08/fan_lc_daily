class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        memo = {}

        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])

            if i in memo:
                return memo[i]

            memo[i] = max(dp(i-1), dp(i-2) + nums[i])
            
            return memo[i]
        
        return dp(len(nums)-1)


class Solution:
    def rob(self, nums: List[int]) -> int:
        # [1,2,3,1]
        memo = {}

        def dp(i):
            if i == 0:
                memo[i] = nums[0]

            if i == 1:
                memo[i] = max(nums[0], nums[1])

            if i in memo:
                return memo[i]

            memo[i] = max(dp(i-1), dp(i-2) + nums[i])
            return memo[i]

        return dp(len(nums)-1)
