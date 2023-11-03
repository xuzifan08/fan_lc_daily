class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1,2,3,4, 5,6,7] k = 3
        # [4,3,2,1, 5,6,7]
        # [4,3,2,1, 7,6,5]
        # [4,3,2,1, 7,6,5]

        k = k % len(nums)
        self.reverse(nums, 0, len(nums) -k-1)
        self.reverse(nums, len(nums)- k, len(nums)-1)
        self.reverse(nums, 0, len(nums)-1)
        return nums


    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1