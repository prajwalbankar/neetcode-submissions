class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        result=[int]
        for num in nums:
            if num in d:
                d[num] = d[num] + 1
            else:
                d[num] = 1
        print(d.items())
        # for key,value in d.items():
        #     if value >= k:
        #         result.append(key)
        value = list(d.values())
        value.sort()
        value.reverse()
    
        result = [value[i] for i in range(k)]

        ans = [key for key, value in d.items() if value in result]
        # reverse_d = {v : k for k, v in d.items()}
        # ans = list(reverse_d.values())
    
        return ans