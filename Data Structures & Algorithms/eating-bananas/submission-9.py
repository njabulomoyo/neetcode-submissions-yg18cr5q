class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        k = r
        #[1,4,3,2]
        while l<r:
            total = 0
            mid = (l+r)//2 # mid = 2
            for elem in piles: #elem = 2
                hrs = math.ceil(elem/mid) # hrs = 1
                total += hrs # 6

            if total > h:
                l = mid + 1
                
            else:
                r = mid 
                k = mid
            print(k)
        
        return k

