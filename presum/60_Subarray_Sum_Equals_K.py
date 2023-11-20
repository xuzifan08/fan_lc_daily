class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [1,2,3]
        sum_count = {0:1}
        presum = 0
        total = 0

        for num in nums:
            presum += num

            if presum - k in sum_count:
                total += sum_count[presum - k]

            if presum in sum_count:
                sum_count[presum] += 1
            else:
                sum_count[presum] = 1
        return total