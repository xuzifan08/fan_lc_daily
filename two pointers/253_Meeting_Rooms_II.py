class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # [[0,                30], 
        #    [5, 10], ]
        #.           [15, 20]
        start = sorted([interval[0] for interval in intervals])
        end = sorted([interval[1] for interval in intervals])

        res, count = 0,0
        s,e = 0,0

        while s < len(start):
            if start[s] < end[e]:
                count += 1
                res = max(res, count)
                s += 1
            elif start[s] == end[e]:
                s += 1
                e += 1 
            else:
                count -= 1
                e += 1

        return res