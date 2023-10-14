class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        left = 0
        right = len(nums) - 1
        memo = collections.defaultdict(int)
        
        def max_diff(left, right):
            if left == right:
                return nums[left]
            if (left, right) in memo:
                return memo[(left, right)]

            max_left = nums[left] - max_diff(left + 1, right)
            max_right = nums[right] - max_diff(left, right-1)

            memo[(left, right)] = max(max_left, max_right)

            return memo[(left, right)]

        return max_diff(left, right) >= 0 
