class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        #[-4,-1,-1,0,1,2]
        i=0
        result=[]
        while i<len(nums)-2:
            left = i+1
            right = len(nums)-1
            target= -1*sorted_nums[i]
            while left<right:
                if sorted_nums[left] + sorted_nums[right] == target and [sorted_nums[i], sorted_nums[left], sorted_nums[right]] not in result:
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    continue
                if sorted_nums[left] + sorted_nums[right] < target:
                    left += 1
                else:
                    right -= 1
            i += 1  


        return result