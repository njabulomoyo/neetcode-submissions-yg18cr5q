class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for i in range(len(prices)-1):
            for j in range(i,len(prices)):
                profit = prices[j] - prices[i]
                print(f"profit is {profit}")
                res = max(res,profit)
            print(res)
        
        return res


        