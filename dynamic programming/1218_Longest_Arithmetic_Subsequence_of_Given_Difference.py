class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        ans = 1
        # [1,5,7,8,5,3,4,2,1], -2
        #          
        # dp{1:1, 5:2, 7:1, 8:1, 3: 3, 4:1,  2:1,  }
        for i in range(len(arr)):
            if arr[i] - difference in dp:
                dp[arr[i]] = dp[arr[i] - difference] + 1

            else:
                dp[arr[i]]  = 1
            ans = max(ans, dp[arr[i]])

        return ans