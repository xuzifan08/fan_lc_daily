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
    



class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # [[0,                30], 
        #    [5, 10], ]
        #.           [15, 20]
        starts = sorted([interval[0] for interval in intervals])
        ends = sorted([interval[1] for interval in intervals])
        # [0,5,15]
        # [10,20,30]

        s = 0
        e = 0
        room = 0
        max_room = 0

        while s < len(ends):

            if starts[s] < ends[e]:
                room += 1
                s += 1
                max_room = max(max_room, room)
            elif starts[s] == ends[e]:
                s += 1
                e += 1
            else:
                room -= 1
                e += 1
                max_room = max(max_room, room)

        return max_room
                