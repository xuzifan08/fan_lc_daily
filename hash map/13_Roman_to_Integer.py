class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        check = {"I": 1, 
                 "V": 5,
                 "X": 10,
                 "L": 50,
                 "C": 100,
                 "D": 500,
                 "M": 1000}

        for i in range(len(s) - 1):
            if check[s[i]] < check[s[i + 1]]:
                res -= check[s[i]]
            else:
                res += check[s[i]]
        
        return res + check[s[-1]]
    
class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        check = {"I": 1, 
                 "V": 5,
                 "X": 10,
                 "L": 50,
                 "C": 100,
                 "D": 500,
                 "M": 1000}
        
        for i, c in enumerate(s[:-1]):
            if check[c] < check[s[i + 1]]:
                res -= check[c]
            else:
                res += check[c]

        res += check[s[-1]]
        return res
