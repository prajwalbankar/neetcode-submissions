class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #,
        #-4,-3,-2,-1,-1,0,0,1,2,3,4
        #[-3,-1,4],[-3,0,3],[-2,-1,3],[-1,-1,2]

        i=0
        left = 1
        right = len(nums) -1
        result=[]
        nums.sort()

        for i in range(0,len(nums)-2,1):
            left = i+1
            right = len(nums)-1
            while right>left:
                if nums[i] + nums[left] + nums[right] == 0: 
                    if [nums[i], nums[left], nums[right]] not in result:
                        result.append([nums[i], nums[left], nums[right]])

                if nums[i] + nums[left] + nums[right] > 0: right -= 1
                else: left += 1
        
        return result