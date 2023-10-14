class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [float('inf')] * (n + 1)

        dp[0] = 0

        for i in range(n + 1):
            left_most = max(0, i - ranges[i])
            right_most = min(n, i + ranges[i])

            for j in range(left_most, right_most + 1):
                dp[right_most] = min(dp[right_most], dp[j] + 1)
        if dp[-1] == float('inf'):
            return -1

        return dp[n]
