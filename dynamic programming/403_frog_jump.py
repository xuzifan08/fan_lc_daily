class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # [0,1,3,5,6,8,12,17]
        end = stones[-1]
        stones = set(stones)
        
        
        cache = {}
        def dp(current, step):
            if current == end:
                return True
            if (current, step) in cache:
                return cache[(current, step)]

            next_step = current + step

            if next_step in stones and next_step!= current:
                cache[(next_step, step)] = dp(next_step, step)
                if dp(next_step, step):
                    return True

            if step-1 >= 0 and next_step - 1 in stones and next_step!=current:
                cache[(next_step-1, step-1)] = dp(next_step-1, step-1)
                if dp(next_step-1, step-1):
                    return True
            if next_step + 1 in stones:
                cache[(next_step+1, step+1)] = dp(next_step+1, step+1)
                if dp(next_step+1, step+1):
                    return True

            return False

        return dp(0,0)