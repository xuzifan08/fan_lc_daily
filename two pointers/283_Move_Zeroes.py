class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1,3,0,0,12]
        #.   w 
        #.     r
        # [1,0,0,3,12]
        #. 
        # [1,3,0,0,12]
        #. 
        # [1,3,12,0,0]
        write = 0
        read = 0

        while read < len(nums):
            if nums[write] == 0:
                if nums[read]!=0:
                    nums[write], nums[read] = nums[read], nums[write]
                    write += 1
                read += 1
            elif nums[write]!=0:
                write += 1
                read += 1

        return nums
    

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1,3,12,0,0,0,1,9,0]
        #.        w 
        #.          r

        write = 0
        read = 0

        while read < len(nums):
            if nums[write] != 0:
                write += 1
            elif nums[write] == 0 and nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
            read += 1
        return nums
