class Solution:
    """
    output: int max amount of water

    solution:
    - initiate two pointers, l, r
    - initiate maxcount var
    - check the area under the two pointers, (r-l)*min height of the two
    - then move which ever pointers is smaller
    - do this while l < r
    - return max amount recorded
    """
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights)-1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(area, res)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res
        