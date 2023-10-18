class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        # [20,1,15,3,10,5,8]
        #.         r
        #. l
        for right in range(len(nums)):
            for left in range(right):
                diff = nums[right] - nums[left]
                if (left, diff) in dp:
                    dp[(right, diff)] = dp[(left, diff)] + 1
                else:
                    dp[(right, diff)] = 2


        return max(dp.values())


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # [20,1,15,3,10,5,8]
        # longest seq -> seq[i + 1] - seq[i] is the same value
        dp = {} # (index, diff):length

        for right in range(len(nums)):
            for left in range(right):
                diff = nums[right] - nums[left]
                if (left, diff) in dp:
                    dp[(right, diff)] = dp[(left, diff)] + 1
                else:
                    dp[(right, diff)] = 2

        return max(dp.values())

