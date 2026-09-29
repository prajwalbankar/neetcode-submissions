class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashset = set()
        # sorted_s = ''.join(sorted(s))
        # sorted_t = ''.join(sorted(t))

        # if sorted_s==sorted_t: return True
        # else: return False
        if(len(s) != len(t)): return False
        d = {}
        for c in s:
            d[c] = 1 + d.get(c,0)
        print(d.items())
        for c in t:
            if d.get(c) : d[c] = d[c] - 1
            else : return False
        
        return True

