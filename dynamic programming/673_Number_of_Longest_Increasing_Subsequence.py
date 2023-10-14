class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        #        [1,3,5,4,7]
        #.            i j
        # max_len
        # count
        dp = {}

        lenLIS = 0
        res = 0

        for i in range(len(nums) - 1, -1, -1):
            max_len, max_count = 1, 1

            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    length, count = dp[j]
                    if 1 + length > max_len:
                        max_len = 1 + length
                        max_count = count
                    elif 1 + length == max_len:
                        max_count += count
            if max_len > lenLIS:
                lenLIS = max_len
                res = max_count
            elif max_len == lenLIS:
                res += max_count

            dp[i] = [max_len, max_count]

        return res


