class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [1,2,3]
        pre_sum = collections.defaultdict(int)
        pre_sum[0] = 1

        res = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num

            if curr_sum - k in pre_sum:
                res += pre_sum[curr_sum - k]
            pre_sum[curr_sum] += 1

        return res