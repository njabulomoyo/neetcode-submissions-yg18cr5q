class Solution:
    """
    understand:
    input - list
    output - boolean
    time o(n) and space o(1)
    """
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for i in nums:
            if i in numSet:
                return True
            numSet.add(i)

        return False