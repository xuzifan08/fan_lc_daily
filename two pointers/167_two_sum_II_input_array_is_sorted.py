class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [2,7,11,15]

        left = 0
        right = len(numbers)-1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left+1, right+1]

        return []
    
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [2,7,11,15]

        l = 0
        r = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]