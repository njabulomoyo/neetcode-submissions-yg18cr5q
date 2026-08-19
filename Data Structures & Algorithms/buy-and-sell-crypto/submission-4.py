class Solution:
    """
    output: int - max profit
    edge cases: no unique numbers- no sell

    Solution:
    - initiate mx profit var
    - initiate two pointers, fast and slow pointer
    - fast moves each iteration
    - slow moves to fast when fast is less than slow
    - with each move (slow), find diff btween slow and fast, 
    - keep track of the max
    - return max profit
    """
    def maxProfit(self, prices: List[int]) -> int:
        mxp = 0
        slow, fast = 0, 0
        while fast < len(prices):
            if prices[slow] > prices[fast]:
                slow = fast
            elif prices[slow] < prices[fast]:            
                dif = prices[fast] - prices[slow]
                mxp = max(mxp, dif)

            fast += 1
        return mxp

            