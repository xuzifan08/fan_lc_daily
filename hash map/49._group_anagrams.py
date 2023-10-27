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


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = collections.defaultdict(list)

        for word in strs:
            list_key = [0] * 26
            for c in word:
                list_key[ord(c) - ord('a')] += 1
            hash_map[tuple(list_key)].append(word)

        return hash_map.values()
