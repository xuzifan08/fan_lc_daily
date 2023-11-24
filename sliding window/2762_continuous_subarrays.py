class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        cnt = collections.defaultdict(int)
        i = 0
        res = 0
        # [5,4,1,4]
        
        for j, num in enumerate(nums):
            cnt[num] += 1

            while max(cnt) - min(cnt)> 2:
                cnt[nums[i]] -= 1
                if cnt[nums[i]] == 0:
                    del cnt[nums[i]]
                i += 1

            res += j - i + 1

        return res