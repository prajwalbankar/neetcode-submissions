class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # d = set()
        # res=set()
        # if len(nums) == 1: return 1
        # for num in nums:
        #     d.add(num)
        #     if (num-1 in d) or (num+1 in d) :
        #         res.add(num)
        #         res.add(num-1)
        # print(res)
        # return len(res)
        nums_set = set(nums)
        longest = 0

        for num in nums:
            #check if its start of the seq
            if num-1 not in nums_set:
                length = 0
                while (num + length) in nums_set:
                    length += 1
                longest = max(length, longest)
        return longest

                 