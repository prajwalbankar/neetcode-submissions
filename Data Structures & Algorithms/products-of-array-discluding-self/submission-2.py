class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # result=[]
        # for i in range(len(nums)):
        #     mul=1
        #     for j in range(len(nums)):
        #         if j==i : continue
        #         mul=mul*nums[j]
        #     result.append(mul)
        # return result
        prefix=[]
        mul=1
        for i in range(len(nums)):
            if i==0 : 
                prefix.append(1)
                continue
            mul = mul * nums[i-1]
            prefix.append(mul)
        # print(prefix)  //[1,1,2,8]

        suffix=[0]*(len(nums))
        mul=1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                suffix[i]=mul
                continue
            mul = mul * nums[i+1]
            suffix[i] = mul
        
        result=[0] * len(nums)
        for i in range(len(nums)):
            result[i] = prefix[i] * suffix[i]
        return result

