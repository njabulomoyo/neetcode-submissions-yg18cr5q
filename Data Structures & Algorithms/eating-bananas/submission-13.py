import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l<=r:
            mid=(l+r)//2
            if self.checkValidRate(mid,h,piles):
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        return result        

    def checkValidRate(self,n,k,lst):
        total = 0
        for i in lst:
            p = math.ceil(i/n)
            total += p
        if total > k:
            return False
        else:
            return True


        