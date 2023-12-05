class Solution:
    def firstUniqChar(self, s: str) -> int:
        last_occurence = {v:i for i, v in enumerate(s)}
        seen = set()

        for idx, v in enumerate(s):
            if v not in seen:
                if last_occurence[v]==idx:
                    return idx
                else:
                    seen.add(v)
        return -1