class Solution:
    def minDeletions(self, s: str) -> int:
        count = collections.Counter(s)
        see_freq = set()

        res = 0

        for v, cnt in count.items():
            while cnt > 0 and cnt in see_freq:
                cnt -= 1
                res += 1
            see_freq.add(cnt)

        return res
    
import heapq
class Solution:
    def minDeletions(self, s: str) -> int:
        count = collections.Counter(s)
        freq = count.values()
        freq = [-f for f in freq if f != 0]
        heapq.heapify(freq)

        delete = 0
        while len(freq) > 1:
            top = -heapq.heappop(freq)
            
            if top == -freq[0]:
                if top - 1 > 0 :
                    top -= 1
                    heappush(freq, -top)

                delete += 1

        return delete