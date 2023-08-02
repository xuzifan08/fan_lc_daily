class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        forward_stack = []
        min_bound = len(nums)
        max_bound = 0
        backward_stack = []

        for i in range(len(nums)):
            while forward_stack and nums[forward_stack[-1]] > nums[i]:
                curr_idx = forward_stack.pop()
                min_bound = min(curr_idx, min_bound)
            forward_stack.append(i)
        
        for j in reversed(range(len(nums))):
            while backward_stack and nums[backward_stack[-1]] < nums[j]:
                curr_idx = backward_stack.pop()
                max_bound = max(max_bound, curr_idx)
            backward_stack.append(j)

        return max_bound - min_bound + 1 if max_bound - min_bound > 0 else 0

