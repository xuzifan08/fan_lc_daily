class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        
        def half_isom(s, t):
            look_up = {}
            
            for i in range(len(s)):
                if s[i] not in look_up:
                    look_up[s[i]] = t[i]
                elif look_up[s[i]] != t[i]:
                    return False
                
            return True

        return half_isom(s, t) and half_isom(t, s)
