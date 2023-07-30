class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)
        word_count = collections.Counter(words)
        word_length = len(words[0])
        substring_size = word_length * k

        ans = []

        def sliding_window(left):
            word_used = 0
            excess_word = False
            word_found = collections.defaultdict(int)
            
            for right in range(left, n, word_length):
                if right + word_length > n:
                    break

                sub = s[right: right + word_length]
                if sub not in word_count:
                    word_used = 0
                    excess_word = False
                    word_found = collections.defaultdict(int)
                    left = right + word_length
                else:
                    while right -left == substring_size or excess_word:
                        left_most = s[left :left + word_length]
                        left += word_length
                        word_found[left_most] -= 1

                        if word_found[left_most] == word_count[left_most]:
                            excess_word = False
                        else:
                            word_used -= 1
                    word_found[sub] += 1
                    if word_found[sub] <= word_count[sub]:
                        word_used+=1
                    else:
                        excess_word = True
                    
                    if word_used == k and not excess_word:
                        ans.append(left)


        for i in range(word_length):
            sliding_window(i)
        return ans