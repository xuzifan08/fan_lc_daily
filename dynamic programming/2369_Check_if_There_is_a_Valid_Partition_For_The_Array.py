class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        # [4, 4, 4,5,6]
        #.    f  t f f
        two = nums[-1] == nums[-2]
        if len(nums)==2:
            return two
        three = (nums[-1] == nums[-2] == nums[-3]) or (nums[-3] + 1 == nums[-2] == nums[-1] - 1)

        dp = [three, two, False]


        for i in range(len(nums) - 4, -1, -1):
            curr = (nums[i] == nums[i + 1] and dp[1])

            curr = curr or ((nums[i] + 1 == nums[i+1] == nums[i+2] - 1 or  nums[i] == nums[i+1] == nums[i+2]) and dp[2])
            dp = [curr, dp[0], dp[1]]

        return dp[0]