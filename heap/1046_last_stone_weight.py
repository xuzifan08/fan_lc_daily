import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones)>=2:
            first = - heapq.heappop(stones)
            second = - heapq.heappop(stones)

            if first != second:
                heapq.heappush(stones, -(first -second))

        return -stones[0] if stones!=[] else 0
    

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heaviest two stones but python heapq only implement min heap
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones) * (-1)
            second = heapq.heappop(stones) * (-1)
            if first != second:
                smash = -1 * abs(first - second)
                heapq.heappush(stones, smash)
        return -stones[0] if len(stones) else 0
