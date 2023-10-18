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



class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        #        [1,3,5,4,7]
        #.              i j
        glo_len=0
        glo_count = 0

        dp = {}
        # dp[i] = [max_len, max_count]
        for i in range(len(nums)-1, -1, -1):
            max_len = 1
            max_count = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    cur_len, cur_cnt = dp[j]
                    if 1 + cur_len > max_len:
                        max_len = 1 + cur_len
                        max_count = cur_cnt
                    elif 1 + cur_len == max_len:
                        max_count += cur_cnt
            
            if max_len > glo_len:
                glo_len = max_len
                glo_count = max_count
            elif max_len == glo_len:
                glo_count += max_count
            dp[i] = [max_len, max_count]

        return glo_count