class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = 1
        cur_min = 1
        res = max(nums)

        for n in nums:
            if n == 0:
                cur_max = 1
                cur_min = 1

            temp = cur_max * n
            cur_max = max(cur_max*n, cur_min*n, n)
            cur_min = min(temp, cur_min*n, n)
            res = max(res, cur_max)

        return res