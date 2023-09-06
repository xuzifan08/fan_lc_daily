class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map  = {"2":'abc', "3":'def', "4":'ghi', "5":'jkl', "6":'mno', "7":'pqrs', "8":'tuv', "9":'wxyz'}

        res = []

        def backtrack(currStr, i):
            if len(digits) == len(currStr):
                res.append(currStr)
                return

            for c in phone_map[digits[i]]:
                currStr = currStr + c
                backtrack(currStr, i + 1)
                currStr = currStr[:-1]

        if digits:
            backtrack("", 0)

        return res