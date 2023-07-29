class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1]!=nums[i]:
                self.two_sum(nums, i, res)
        return res

    def two_sum(self, nums: List[int], i: int, res:List[List[int]]):
        lo = i+1
        hi = len(nums) - 1

        while lo < hi:
            summation = nums[i] + nums[lo] + nums[hi]

            if summation > 0:
                hi -= 1
            elif summation < 0:
                lo += 1

            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -=1

                while lo < hi and nums[lo] == nums[lo-1]:
                    lo += 1
