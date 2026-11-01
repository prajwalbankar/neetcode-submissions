class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        max_height=0
        while i<j:
            max_height = max(max_height,(j-i)*min(heights[j],heights[i]))
            if heights[i] > heights[j]:
                j-=1
            elif heights[j] > heights[i]:
                i+=1
            else: 
                j-=1
                i+=1
        return max_height
