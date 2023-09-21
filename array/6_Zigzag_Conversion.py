class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        # "P AYPAL I SHIRI N G"
        str_list = [""] * (numRows)
        # str_list[0] += s[0]

        directions = 1
        num_count = 0

        for i in range(len(s)):
            if directions > 0:
                str_list[num_count] += s[i]
                num_count += 1
                if num_count == numRows:
                    directions = -1
                    num_count -= 2

            elif directions < 0:
                str_list[num_count] += s[i]
                num_count -= 1
                if num_count == -1:
                    directions = 1
                    num_count += 2
        res = ""
        for string in str_list:
            res += string

        return res