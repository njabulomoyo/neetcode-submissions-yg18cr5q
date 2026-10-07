class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)
        #h=4
        while l <= r:
            rate = (l+r)//2 #rate= 1+2//2=1
            hrs = 0
            
            for bananas in piles:
                hr = bananas//rate if bananas%rate==0 else 1+bananas//rate  
                hrs += hr
            if hrs <= h:
                res = rate
                r = rate-1
            else:                    
                l = rate + 1
                
        return res
