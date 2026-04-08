class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxLeft, maxRight = height[l], height[r]
        res = 0
        while l < r:
            if maxLeft <= maxRight:
                l += 1
                maxLeft = max(maxLeft,height[l])                
                diff = maxLeft-height[l]
                res += diff 
                
            else:
                r-= 1
                maxRight = max(maxRight,height[r])
                
                diff = maxRight - height[r]
                res += diff 
                
        
        return res














        """
        maxLeft = [0]* len(height) 
        maxRight = [0]* len(height) 
        m = 0
        
        for i in range(len(height)):
            maxLeft[i] = m
            m = max(m,height[i])
          

        n=0
        for i in range(len(height)-1,-1,-1):
            maxRight[i] = n
            n = max(n,height[i])
         

        res = 0
        for i in range(len(height)):
            diff = min(maxLeft[i],maxRight[i]) - height[i]
            print(f"it is the {i}th iteration and res is {res} ")
            if diff > 0:
                res += diff

        return res
        """


            


                