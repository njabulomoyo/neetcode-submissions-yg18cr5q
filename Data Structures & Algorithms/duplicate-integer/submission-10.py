class Solution:
    """
    understand:
        output - bool
        edge cases?
        empty list? no

    """
    def hasDuplicate(self, nums: List[int]) -> bool:
        return not len(nums) == len(set(nums))