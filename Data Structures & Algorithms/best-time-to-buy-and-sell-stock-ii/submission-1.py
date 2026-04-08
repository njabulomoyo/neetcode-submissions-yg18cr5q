class Solution:
    """
    Plan:
    have 2 pointers, slow and fast pointer, start at beginning
    fast pointer will check if next elem is >= slow
    if true continue, move pointer
    if false, calculate profit, save it
    move slow pointer to fast pointer
    do this until the end
    return total profit
    """
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i]-prices[i-1])
        return profit









        