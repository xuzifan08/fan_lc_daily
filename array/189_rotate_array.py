class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 3
        # 0 1 2 3 4 5 6
        #[1,2,3,4,5,6,7]
        #[5,6,7,1,2,3,4]
        n = len(nums)
        k = k % n

        nums[:] = nums[n-k:] + nums[:n-k]

        return nums


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        k = k % len(nums)
        # 3
        # 0 1 2 3 4 5 6
        #[1,2,3,4,5,6,7]
        #[5,6,7,1,2,3,4]
        self.reverse(0, len(nums)-1, nums)
        self.reverse(0, k-1, nums)
        self.reverse(k, len(nums)-1, nums)

        
    def reverse(self, left, right, nums):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
