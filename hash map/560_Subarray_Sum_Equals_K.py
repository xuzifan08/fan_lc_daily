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
    
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [1,2,3]
        presum = collections.defaultdict(int)
        presum[0] = 1

        runing_sum = 0
        res = 0

        for num in nums:
            runing_sum += num

            if runing_sum - k in presum:
                res += presum[runing_sum - k]

            presum[runing_sum] += 1

        return res