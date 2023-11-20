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

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i == 0 or nums[i]!= nums[i-1]:
                self.two_sum(i, nums, res)
        return res
    def two_sum(self, i, nums, res):
        
        left = i + 1
        right = len(nums) - 1
        print(i, left, right)
        while left < right:
            summ = nums[i] + nums[left] + nums[right]

            if summ > 0:
                right -= 1
            elif summ < 0:
                left += 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left-1]:
                    left += 1

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def two_sum(nums, i):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1

                else:
                    right -= 1

        nums.sort()
        res = []
        # [-4, -1, -1, 0, 1, 2]
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i == 0  or nums[i]!=nums[i-1]:
                two_sum(nums, i)
        return res





class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # [-4, -1, -1, 0, 1, 2]
        res = []

        def two_sum(i, nums):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i == 0 or nums[i] != nums[i-1]:
                two_sum(i, nums)

        return res