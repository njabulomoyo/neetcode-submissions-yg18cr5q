class Solution:
    """
    output - int (maximum amount that can be retained)
    edge cases?
    same bar height?
    empty list? No

    Plan:
        1. have two pointers, one at the beginning and one at the end
        2. get the amount that can be contained in by those pointers
        3. after check, move pointer that has a height that is longer
        4. do this wjile left pointer is less than the right pointer
        5. kepp track of the greatest/ max area under any two pointers
        6. return max area

    """
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            length = min(heights[l], heights[r])
            cap = (r - l) * length

            print(length)
            res = max(res, cap)
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] <= heights[r]:
                l += 1

        return res

        