class Solution:
    """
    output: int(maximum profit)
    brainstorm:
    -go thru the whole list
    -keep track of the max profit
    -two pointers, slow and fast
    -fast moves to find higher prices

    -edge case? 
    -if prices are same? return 0
    -prices, never go up? return 0
    -no input? return 0
    -
    """
    def maxProfit(self, prices: List[int]) -> int:
        slow = 0
        maxProfit = 0

        for fast in range(len(prices)):       
            if prices[slow] >= prices[fast]:
                slow = fast
            else:
                profit = prices[fast] - prices[slow]
                maxProfit = max(profit, maxProfit)
        return maxProfit
                



