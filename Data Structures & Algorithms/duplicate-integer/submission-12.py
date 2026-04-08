class Solution:
    """
    - iterate thru The whole thing
    - initiate a set
    - as you iterate through the array, check if current char already in
    set or not
    - if you find char already in set,
    - return True, 
    - otherwise continue
    - iterate till the end of the array
    """
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for char in nums:
            if char in numSet:
                return True
            numSet.add(char)
        return False




        