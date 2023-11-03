class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * (len(nums))
        ptr = len(nums) - 1

        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] * nums[left] < nums[right] * nums[right]:
                res[ptr] = nums[right] * nums[right]
                right -= 1

            else:
                res[ptr] = nums[left] * nums[left]
                left += 1
            ptr -= 1

        return res