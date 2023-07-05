class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_magazine = collections.defaultdict(int)
        freq_ransom = collections.defaultdict(int)

        for c in magazine:
            freq_magazine[c] += 1

        for c in ransomNote:
            freq_ransom[c] += 1

        for c in ransomNote:
            if freq_magazine[c] < freq_ransom[c]:
                return False
        
        return True