class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(curr, summ, i):
            if summ == target:
                res.append(curr[:])
                return

            if summ > target:
                return

            for i in range(i, len(candidates)):
                curr.append(candidates[i])
                summ += candidates[i]
                backtrack(curr, summ, i)
                curr.pop()
                summ -= candidates[i]
        backtrack([], 0, 0)

        return res


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(curr, summ, i):
            if summ == target:
                res.append(curr[:])

            if summ > target:
                return

            for j in range(i, len(candidates)):
                summ += candidates[j]
                curr.append(candidates[j])
                backtrack(curr, summ, j)
                summ -= candidates[j]
                curr.pop()

        backtrack([],0,0)
        return res