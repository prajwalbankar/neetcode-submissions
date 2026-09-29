class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        #Count Frequency
        for num in nums:
            d[num] = 1 + d.get(num,0)

        #Create buckets
        freq = [[] for i in range(len(nums) + 1)]
        for num, count in d.items():
            freq[count].append(num)

        #Collect top k
        res=[]
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k: return res
        
