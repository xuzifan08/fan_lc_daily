class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10**9 + 7
        #  words = ["acca","bbbb","caca"], target = "aba"
        cnt = defaultdict(int)
        for w in words:
            for i, c in enumerate(w):
                cnt[(i, c)] += 1 # i is the index of all the words, c is the value of the specific index

        cache = {}

        def dp(i, k): # i is the index of target, k is index of words
            if i == len(target):
                return 1

            if k == len(words[0]):
                return 0

            if (i, k) in cache:
                return cache[(i, k)]

            # transition 
            # skip this char
            cache[(i, k)] = dp(i, k+1)
            # not skip this char
            cache[(i, k)] += cnt[(k, target[i])] * dp(i + 1, k+1)

            return cache[(i, k)] % mod


        return dp(0, 0)# number of ways to form the target