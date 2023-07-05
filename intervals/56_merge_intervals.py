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