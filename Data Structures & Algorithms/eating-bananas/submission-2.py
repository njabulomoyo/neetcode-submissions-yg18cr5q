class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # l=4, r=3
        res = r #11
        
        
        while l<=r:
            hours = 0
            k = (l+r)//2 #k = 4
            for i in piles:
                hours += math.ceil(i/k) #1+2+2+3

            if hours <= h:
                res = min(res,k)# res = 4
                r = k - 1 #r = 3
            else:
                l =  k + 1#l=4

        return res 


        