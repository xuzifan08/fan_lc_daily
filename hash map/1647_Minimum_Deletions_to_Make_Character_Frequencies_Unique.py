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