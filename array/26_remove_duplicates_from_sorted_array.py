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
    

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [0,1,2,1,1,2,2,3,3,4]
        #        w
        #.               r 
        write = 0
        read = 0

        while read < len(nums):
            while read < len(nums) and nums[write] == nums[read]:
                read += 1
            if read < len(nums) and nums[read]!= nums[write]:
                write += 1
                nums[write] = nums[read]
                read += 1

        return write + 1
    


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [0,1,1,1,1,2,2,3,3,4]
        #    w
        #.       r
        w = 0
        r = 0

        while r < len(nums):
            while r < len(nums) and nums[w] == nums[r]:
                r += 1
            if  r < len(nums) and nums[w] != nums[r]:
                w += 1
                nums[w] = nums[r]
                r += 1
        return w+1
    

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [0,1,1,1,1,2,2,3,3,4]
        #.   w
        #.       r
        # [1,2,2]
        #.   w
        #.       r

        write = 0
        read = 1

        while read < len(nums):
            if nums[write] != nums[read]:
                write += 1
                nums[write] = nums[read]
            read += 1


        return write + 1
