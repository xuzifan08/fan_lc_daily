class Solution:
    def compress(self, chars: List[str]) -> int:
        # ["a","2","b","2","c","c","c"]
        #                   w
        #.                             r
        #.  c = 3
        write = 0
        read = 0
        count = 0
        while read <= len(chars):
            if read < len(chars):
                if read == 0 or chars[read] == chars[read-1]:
                    count += 1
                    read += 1
                elif chars[read]!= chars[read-1]:
                    chars[write] = chars[read-1]
                    write += 1
                    if count > 1:
                        count_str = str(count)
                        for i in count_str:
                            chars[write] = i
                            write += 1
                    read += 1
                    count = 1
            elif read == len(chars):
                chars[write] = chars[read-1]
                write += 1
                if count > 1:
                    count_str = str(count)
                    for i in count_str:
                        chars[write] = i
                        write += 1
                return write