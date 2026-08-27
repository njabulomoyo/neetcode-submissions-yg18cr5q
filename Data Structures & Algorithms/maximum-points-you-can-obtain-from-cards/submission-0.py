class Solution:
    """
    output: int - max points from cards picked

    edge cases? no empty list. same element

    Solution:
    - initiate a window of size len(lst)-1-k
    - then calculate the some of the elemnts outside the window
    - keep a variable to track the maximum points
    - move the window until the right pointer == len(lst)
    """
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l, r = 0, len(cardPoints)-1-k
        res = 0
        while r < len(cardPoints):
            total = 0
            if l > 0:
                for elem in cardPoints[:l]:
                    total += elem
            if r <len(cardPoints):
                for elem in cardPoints[r+1:]:
                    total += elem
            res = max(res, total)
            l += 1
            r += 1
            
        return res
        