class Solution:
    """
    output - boolean
    edge cases? [] == False
    Find the duplicate: return True if yes, otherwise fasle
    Solution:
    - initiate a set
    - iterate thru list
    - for each item, check if it exists on set
    - if yes, return True
    - else, continue
    - do this for all the numbers
    - return False

    """
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for elem in nums:
            if elem in s:
                return True
            s.add(elem)

        return False




        