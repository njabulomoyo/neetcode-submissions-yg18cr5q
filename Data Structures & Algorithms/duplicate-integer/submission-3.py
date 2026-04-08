class Solution:
    '''
    understand:
    - empty list?
    - expected time and space complexity ? o(n) time and space
    Match:
    - dictionaries or sets

    '''
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for i in nums:
            if i in nums_set:
                return True
            nums_set.add(i)
        return False
        
         