class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > ceil(hour):
            return -1
        
        def check(speed):
            h = 0

            for dis in dist[:-1]:
                h += ceil(dis / speed)

            h += dist[-1] / speed
            
            return h <= hour 

        
        left = 1
        right =  10**7

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1   

        return left 