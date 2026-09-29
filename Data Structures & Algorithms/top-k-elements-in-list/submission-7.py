from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = defaultdict(int)
        result=[]
        for n in nums:
            frequency_dict[n] += 1

        sorted_frequency_dict = dict(sorted(frequency_dict.items(),key = lambda item: item[1], reverse=True))
        for key in sorted_frequency_dict.keys():
            result.append(key)
            if len(result)==k:
                return result
            