class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use list as key to group anagrams
        group_anagrams = collections.defaultdict(list)
        print(ord('a'))
        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char)-ord('a')] += 1
            group_anagrams[tuple(freq)].append(word)
            
        return group_anagrams.values()
        

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use list as key to group anagrams
        group_anagrams = collections.defaultdict(list)

        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            group_anagrams[tuple(freq)].append(word)

        return group_anagrams.values()
