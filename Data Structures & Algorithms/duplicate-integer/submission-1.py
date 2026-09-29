class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for num in nums:
        #     if nums.count(num)>1 : return True
        
        # return False

        hashset=set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
