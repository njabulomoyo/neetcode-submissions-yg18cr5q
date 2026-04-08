class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for elem in nums:
            if elem in nums_set:
                return True
            nums_set.add(elem)
        return False
        

         