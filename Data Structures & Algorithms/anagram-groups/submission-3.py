from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars = defaultdict(list)

        for s in strs:
            sorted_s = tuple(sorted(s))
            chars[sorted_s].append(s)
        
        return list(chars.values())