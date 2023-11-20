class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # nums = [1,3,-1,-3,5,3,6,7]
        # left =  [0,1,2,3,4,5,6]
        # right = 3-3 = 0
        # output = 

        queue = collections.deque()
        output = []

        for i in range(len(nums)):

            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)

            if i - k >= queue[0]:
                queue.popleft()
            if i >= k - 1:
                output.append(nums[queue[0]])

        

        return output
    

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # [1,[3,-1,-3],5,3,6,7] 3-3 = 0
        #. 0  1. 2. 3
        queue = collections.deque()
        res = []

        for i in range(len(nums)):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)

            if i - k >= queue[0]:
                queue.popleft()

            if i + 1 >= k:
                res.append(nums[queue[0]])

        return res
    


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # [1,[3,-1,-3],5,3,6,7] 3-3 = 0
        #. 0  1. 2. 3
        # keep the non-decreasing numbers in the window

        queue = collections.deque()
        res = []

        for i in range(len(nums)):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            
            queue.append(i)
            if i - queue[0] + 1 > k:
                queue.popleft()
            if i + 1 >= k:
                res.append(nums[queue[0]])


        return res