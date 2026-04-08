class Solution:
    """
    understand:
    -input - list
    - output -  max area 
    expected time and space? 

    Plan:
        1. have two pointers, one at the start and another at the end
        2. calculate area using current pointer heights
        3. compare the two height, move the smaller one
        4. return maximum area
    """
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        res = 0
        while l<r:
           
            area = (r-l)*min(heights[l],heights[r])
            print(area)
            res = max(res,area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return res







