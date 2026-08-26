class Solution:
    """
    output: int - max profit
     Edge cases- list cant be empty?, same elem? return 0

    solution:
    - initiate 2pointers, l and r
    - iterate thru the whole list
    - compare the elements on the two pointers
    - if r > l, calculate profit, and update max profit
    - if r<l, move l to r
    - return max profit
    """
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,0 #l,r = 1,2
        maxp = 0
        while r < len(prices):#r=5
            if prices[l] < prices[r]:
                maxp = max(maxp, prices[r]-prices[l]) #maxp = 6
            else:
                l = r #l = 5
            r += 1     #r= 6
        return maxp

        