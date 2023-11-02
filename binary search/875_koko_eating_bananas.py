class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [30,11,23,4,20]
        def check(k):
            hour = 0
            for bananas in piles:
                hour += ceil(bananas / k)
            return hour <= h
        
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            finish = check(mid)

            if finish:
                right = mid
            elif not finish:
                left = mid + 1

        return left