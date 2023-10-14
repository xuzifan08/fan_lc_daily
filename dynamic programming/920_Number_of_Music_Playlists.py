class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod =10**9 + 7
        cache = {}

        def dp(curr_goal, old_songs):
            if curr_goal == 0 and old_songs == n:
                return 1

            if curr_goal == 0 or old_songs > n:
                return 0
            if (curr_goal, old_songs) in cache:
                return cache[(curr_goal, old_songs)]

            # choose a new song
            res = (n - old_songs) * dp(curr_goal-1, old_songs + 1)

            # choose a old song
            if old_songs > k:
                res += (old_songs - k) * dp(curr_goal - 1, old_songs)

            cache[(curr_goal, old_songs)] = res
            return res % mod
            
        return dp(goal, 0)