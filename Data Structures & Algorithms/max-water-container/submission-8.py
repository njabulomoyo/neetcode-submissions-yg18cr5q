class Solution:
    """
    output - maximum area under two bars
    duplicates across list?
    empty list?

    Plan:

        1. have two pointers
        2. get area under the two pointers, then move pointers
        3. keep trck of the highest area under the pointers we have passed
        4. moving pointers, move pointer if its height is smaller thanthe other
        5. do this for all the heights while left pointer is less than right pointer

        var for max area
        pointers
        for loop
    """
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
        