class Solution:
    """
    output: int

    edge cases: non-empty list, duplicate numbers?

    Solution:
    - iterate thru the list
    - initiate a slow pointer
    - move slow poiter to current index if the cur num is smaller than number at slow pointer
    - otherwise check profit if cur indx > than slow
    - track maximum
    return max
    """
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0
        for ind, val in enumerate(prices):
            if val < prices[l]:
                l = ind
                continue
            profit = val - prices[l]
            res = max(res, profit)

        return res
        