class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = collections.Counter(arr)
        visit = set()

        for key, val in cnt.items():
            if val in visit:
                return False
            else:
                visit.add(val)
        

        return True