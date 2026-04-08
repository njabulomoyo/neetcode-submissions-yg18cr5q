class Solution:
    def maxArea(self, heights: List[int]) -> int:
        biggie = 0        
        for i in range(len(heights)-1):
            for j in range(i+1,len(heights)):
                l = j-i
                w =  min(heights[i],heights[j])
                biggie = max(biggie,w*l)
        
        return biggie


        