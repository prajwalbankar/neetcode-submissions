from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = defaultdict(int)
        for i in nums:
            if i in dupes:
                return True
            dupes[i] += 1
        return False