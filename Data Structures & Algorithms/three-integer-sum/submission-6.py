class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()

        for i in range(0,len(nums)-2,1):
            if nums[i]>0 : break

            if i>0 and nums[i]==nums[i-1]: continue
            
            left = i+1
            right = len(nums)-1

            while right>left:
                if nums[i] + nums[left] + nums[right] == 0: 
                    if [nums[i], nums[left], nums[right]] not in result:
                        result.append([nums[i], nums[left], nums[right]])

                if nums[i] + nums[left] + nums[right] > 0: right -= 1
                else: left += 1
        
        return result