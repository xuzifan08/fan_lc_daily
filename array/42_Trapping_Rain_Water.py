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
    

class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]

        water = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                water += max(0, maxL - height[l])
                maxL = max(maxL, height[l])
            else:
                r -= 1
                water += max(0, maxR - height[r])
                maxR = max(maxR, height[r])               

        return water

# [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]height
#           l              r
# [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]maxL

# [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0]maxR


class Solution:
    def trap(self, height: List[int]) -> int:
        # need the max of the left, right for each column
        max_l = [0] * len(height)
        max_r = [0] * len(height)

        max_l_now = height[0]

        for i in range(1, len(height)):
            max_l[i] = max_l_now
            max_l_now = max(max_l_now, height[i])


        max_r_now = height[-1]

        for j in range(len(height) -2,-1,-1):
            max_r[j] = max_r_now
            max_r_now = max(max_r_now, height[j])
        print(max_l)
        print(max_r)
        water = 0

        for w in range(len(height)):
            water += max(0,min(max_l[w], max_r[w]) - height[w])


        return water
