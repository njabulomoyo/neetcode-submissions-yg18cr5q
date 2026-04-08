class Solution:
    """
    understand:
    -the number of elements represent the number of piles
    -the each number, nums[i], represents the number of bananas in a pile
    - we have to find the lowest number, that is the lowest rate we can finish all the bananas in all piles within h hours
    - the output is the lowest rate
    - expected time complexity is O(logn)

    plan:
    - l, r = 0, pile with the most bananas
    - we will have our mid pointer, which will be the rate for eating the bananas
    - if the rate does not allow us to finish the banans in time, meaning it would take more time to finish the piles, then we move our left pointer to mid + 1
    - if the rate allows us to finish the bananas in time, then we move our right pointer to mid



    
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        l, r = 1, k #l=25, r=25
        #[25,10,23,4]
        while l < r:
            sum = 0
            mid = (l+r)//2 # m = 25
            for i in piles:
                hr = math.ceil(i/mid)
                sum += hr #sum = 5
            
            if sum > h:
                l = mid + 1 #l=25
            else:
                r = mid
        
        return r
