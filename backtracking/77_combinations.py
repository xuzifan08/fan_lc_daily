class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(curr, i):
            if len(curr) == k:
                ans.append(curr[:])
                return

            for num in range(i, n + 1):
                curr.append(num)
                backtrack(curr, num + 1)
                curr.pop()

        backtrack([], 1)
        return ans
    

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(curr, i):
            if len(curr) == k:
                if curr not in ans:
                    ans.append(curr[:])
                return

            for num in range(i, n+1):
                if i not in curr:
                    curr.append(num)
                    backtrack(curr, num+1)
                    curr.pop()
        backtrack([], 1)


        return ans



class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(curr, i):
            if len(curr) == k:
                res.append(curr[:])

            for num in range(i, n+1):
                if num not in curr:
                    curr.append(num)
                    backtrack(curr, num)
                    curr.pop()

        backtrack([],1)

        return res



class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        # [1,2,3,4]

        def backtrack(curr, i):
            if len(curr) == k:
                res.append(curr[:])

            for num in range(i, n + 1):
                curr.append(num)
                backtrack(curr, num + 1)
                curr.pop()
        backtrack([],1)

        return res