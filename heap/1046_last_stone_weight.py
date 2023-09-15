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
