class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height) - 1
        max_l = height[l]
        max_r = height[r]
        water = 0

        while l < r:
            if max_l <= max_r:
                l += 1
                max_l = max(max_l, height[l])
                if min(max_l,max_r) - height[l] > 0:
                    water += (min(max_l,max_r) - height[l])
                
            else:
                r -= 1
                max_r = max(max_r, height[r])
                if (min(max_l,max_r) - height[r]) > 0:
                    water += (min(max_l,max_r) - height[r])
                
        
        return water
    

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height) - 1

        maxL = height[l]
        maxR = height[r]

        water = 0

        while l < r:
            if maxL < maxR:
                l += 1
                water += max(maxL - height[l], 0)
                maxL = max(maxL, height[l])

            else:
                r -= 1
                water += max(maxR - height[r], 0)
                maxR = max(maxR, height[r])

        return water
