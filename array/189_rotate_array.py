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
        