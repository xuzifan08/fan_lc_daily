class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # [[1,3],[2,6],[8,10],[15,18]]
        #.  1 3
        #.   2. 6
        #.        8 10
        #.             15 18
        intervals.sort(key = lambda x: x[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= output[-1][1]:
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start, end])

        return output
    
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # [[1,3],[2,6],[8,10],[15,18]]
        #.  1 3
        #.    2 6
        #.        8 10
        #.             15 18
        intervals = sorted(intervals, key=lambda x:x[0])
        res = []
        start = intervals[0][0]
        end = intervals[0][1]

        for new_start, new_end in intervals[1:]:
            if end < new_start:
                res.append([start, end])
                start = new_start
                end = new_end
            elif new_start <= end <= new_end:
                end = max(end, new_end)
        res.append([start, end])

        return res