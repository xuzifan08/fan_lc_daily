class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        if len(nums) == 1:
            return nums[0] * count[nums[0]]

        dp = [0]*len(nums)
        #[2,3,5,6]
        dp[0] = nums[0] * count[nums[0]]
        if nums[1] - 1 == nums[0]:
            dp[1] = max(dp[0], nums[1] * count[nums[1]])
        else:
            dp[1] = dp[0] + nums[1] * count[nums[1]]
        print(dp)
        for i in range(2, len(nums)):
            if nums[i] - 1 == nums[i-1]:
                dp[i] = max(nums[i] * count[nums[i]] + dp[i-2],dp[i-1])
            else:
                dp[i] = dp[i-1] + nums[i] * count[nums[i]]

        print(dp)
        return max(dp)