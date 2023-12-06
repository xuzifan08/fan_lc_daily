class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            max_area = max(max_area,(right - left) * min(height[right],height[left]))
            if height[right] >= height[left]:
                left += 1
            else:
                right -= 1

        return max_area
    
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            max_water = max(max_water, (right - left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_water
    
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            max_water = max(max_water, (right - left) *min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_water
    

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # [1,8,6,2,5,4,8,3,7]
        max_water = 0
        left = 0
        right = len(height) - 1

        while left < right:
            max_water = max(max_water, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
    

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # [1,8,6,2,5,4,8,3,7]
        left = 0
        right = len(height) - 1

        max_so_far = 0

        while left < right:
            max_so_far = max(max_so_far, (right - left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_so_far