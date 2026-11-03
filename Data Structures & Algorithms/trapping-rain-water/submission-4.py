class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max=[]
        pre_max=0
        for i in range(len(height)):
            pre_max = max(pre_max, height[i])
            prefix_max.append(pre_max)

        suffix_max=[]
        suf_max=0
        for i in range(len(height)-1,-1,-1):
            suf_max = max(height[i],suf_max)
            suffix_max.append(suf_max)
        suffix_max.reverse()
        
        total_rain=0
        for i in range(len(height)):
            water_at_index = min(prefix_max[i],suffix_max[i])-height[i]
            total_rain += water_at_index

        return total_rain