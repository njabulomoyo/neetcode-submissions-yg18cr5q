class Solution:
    """
    output: bool
    Edge cases: empty array? return False

    Solution:
     - iterate thru the list
     - initiate some storage to keep passed elements
     - for each element checked, confirm if there is same element on storage
     - if there is, return True, otherwise continue
     - continue til the end
     - return False
    """
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        numSet = set()
        for elem in nums:
            if elem in numSet:
                return True
            numSet.add(elem)

        return False

        