class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)

        for row in triangle[::-1]:
            for i, v in enumerate(row):
                dp[i] = min(dp[i], dp[i+1]) + v

        return dp[0]