import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        summation = sum(nums)
        curr_sum = summation
        nums = [-num for num in nums]
        heapq.heapify(nums)
        operations = 0

        while curr_sum * 2 > summation:
            operations += 1
            max_val = -heapq.heappop(nums)
            max_val = max_val / 2
            curr_sum = curr_sum - max_val
            heapq.heappush(nums, -max_val)
            
        return operations
    

import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)
        curr_total = sum(nums)
        nums = [-num for num in nums]
        heapq.heapify(nums)
        operations = 0
        
        while curr_total * 2 > total:
            num = -heapq.heappop(nums)
            num = num / 2
            curr_total -= num
            heapq.heappush(nums, -num)
            operations += 1

        return operations