class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0]* len(height) 
        maxRight = [0]* len(height) 
        m = 0
        #print(f"length of height is {len(height)}")

        for i in range(len(height)):
            maxLeft[i] = m
            m = max(m,height[i])
        print(f"maxLeft is {maxLeft}")  

        n=0
        for i in range(len(height)-1,-1,-1):
            maxRight[i] = n
            n = max(n,height[i])
        print(f"maxRight is {maxRight}") 

        res = 0
        for i in range(len(height)):
            diff = min(maxLeft[i],maxRight[i]) - height[i]
            print(f"it is the {i}th iteration and res is {res} ")
            if diff > 0:
                res += diff

        return res


            


                