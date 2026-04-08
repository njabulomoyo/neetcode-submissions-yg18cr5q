class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #[1,7,2,5,4,7,3,6]
        l,r = 0, len(heights)-1
        area = 0
        while l<r:
            width = r - l
            #print("width is,",w)
            length = min(heights[l],heights[r])
            #print("height is,",l)
            area = max(area,length*width)
            #print(area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r-=1
        #area = max(area,length*width)
        return area
        

            


        """
        biggie = 0        
        for i in range(len(heights)-1):
            for j in range(i+1,len(heights)):
                l = j-i
                w =  min(heights[i],heights[j])
                biggie = max(biggie,w*l)
        
        return biggie
        """


        