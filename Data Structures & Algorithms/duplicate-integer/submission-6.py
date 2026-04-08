class Solution:
    """
    UMPIRE
    understand:
    **find duplicates on the list**
    input - list
    output - bool
    edge cases:
    list empty? return False?
    Match:
    - sets
    - dictionary
    - iteration
    Plan:
    1. go through the whole list
    2. add each element to the set
    3. before adding the element, check if there is a duplicate inside?
    4. if there is, return True
    5. otherwise continue
    6. if you finish the whole list, without finding anything, return False


    """

    
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for i in nums:
            if i in nums_set:
                return True
            nums_set.add(i)
        return False

         