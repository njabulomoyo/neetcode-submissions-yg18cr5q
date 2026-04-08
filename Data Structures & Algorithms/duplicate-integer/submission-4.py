class Solution:
    '''
    understand:
    - empty list?
    - expected time and space complexity ? o(n) time and space
    Match:
    - dictionaries or sets

    '''
    def hasDuplicate(self, nums: List[int]) -> bool:
        return not len(nums)==len(set(nums))
        
         