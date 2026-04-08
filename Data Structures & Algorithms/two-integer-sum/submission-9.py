class Solution:
    """
    understand:
    input - list
    output - list for the indices that give target
    empty list?
    is list sorted?
    time o(n) and space o(n) complexity?
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for indx, val in enumerate(nums):
            diff = target - val
            if diff in d:
                return [d[diff],indx]
            d[val] = indx

            