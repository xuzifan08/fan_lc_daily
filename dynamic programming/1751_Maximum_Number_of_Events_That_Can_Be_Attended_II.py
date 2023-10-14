class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort()
        starts = [start for start, end, value in events]

        dp = [[-1] * n for _ in range(k + 1)]


        def dfs(curr_index, count):
            if count == 0 or curr_index == n:
                return 0

            if dp[count][curr_index]!= -1:
                return dp[count][curr_index]

            next_index = bisect_right(starts, events[curr_index][1])
            dp[count][curr_index] = max(dfs(curr_index + 1, count), dfs(next_index, count - 1) + events[curr_index][2])

            return dp[count][curr_index]

        return dfs(0, k)