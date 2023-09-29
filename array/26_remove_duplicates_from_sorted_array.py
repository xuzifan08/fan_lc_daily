class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [0,1,1,1,1,2,2,3,3,4]
        #    w   r
        write = 0
        read = 1

        while read < len(nums):
            if nums[write] == nums[read]:
                read += 1
            else:
                write += 1
                nums[write] = nums[read]
                read += 1
        return write + 1
    

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [0,1,2,1,1,2,2,3,3,4]
        #      w         r
        write = 0
        read = 1

        while read < len(nums):
            if nums[write] == nums[read]:
                read += 1
            else:
                write += 1
                nums[write] = nums[read]
                read += 1
        return write + 1