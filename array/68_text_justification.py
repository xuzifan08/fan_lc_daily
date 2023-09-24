class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = []
        length = 0
        i = 0
        res = []


        while i < len(words):
            # if line complete
            if length + len(line) + len(words[i]) > maxWidth:
                total_spaces = maxWidth - length
                each_spaces = total_spaces // max(1, len(line) - 1)
                remaining = total_spaces % max(1, len(line) - 1)

                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * each_spaces
                    if remaining:
                        line[j] += " "
                        remaining -= 1
                res.append("".join(line))
                line = []
                length = 0

            # if line doesn't complete
            line.append(words[i])
            length += len(words[i])
            i += 1

        last_line = " ".join(line)
        total_space = maxWidth - len(last_line)
        last_line += " " * total_space

        res.append(last_line)

        return res