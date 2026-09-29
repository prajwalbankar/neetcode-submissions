from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=[]
        chars = defaultdict(list)

        for s in strs:
            sorted_s = tuple(sorted(s))
            chars[sorted_s].append(s)

        for value in chars.values():
            result.append(value)
        
        return result