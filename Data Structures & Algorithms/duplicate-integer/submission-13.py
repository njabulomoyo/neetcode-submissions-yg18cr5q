class Solution:
    """
    Looking for a duplicate:
    edge cases:
        empty list? return false
        use a set to check the duplicate

    solution:
        iterate through the list
        add the numbers to the set
        as we add, we check if the number already exists
        if it does, then we return ture
        otherwise, continue
        continue until the end, return False

    """
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        numSet = set()

        for i in nums:
            if i in numSet:
                return True
            numSet.add(i)
            
        return False










        