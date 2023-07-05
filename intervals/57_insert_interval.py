class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
       # intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]] 
       # newInterval = [4,8]
       #. ---
       #.     ---
        new_start = newInterval[0]
        new_end = newInterval[1]

        output = []

        for i in range(len(intervals)):
            if intervals[i][1] < new_start:
               output.append(intervals[i])
            elif intervals[i][1] >= new_start and intervals[i][0] <= new_end:
                new_start = min(intervals[i][0], new_start)
                new_end = max(intervals[i][1], new_end)
            elif new_end < intervals[i][0]:
                output.append([new_start, new_end])
                output += intervals[i:]
                return output
        output.append([new_start,new_end])
        return output