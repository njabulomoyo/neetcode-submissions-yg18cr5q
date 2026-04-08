class Solution:
    """
    Understand:
    - Input - array
    - output - bool
    edge cases
    empty list? return false
    
    Match: 
    - iteration
    -dictionary/set
    Plan:
    1. create a set
    2. iterate through the set
    3. check if current number exist inside the set
    4. if not add the number to the set and move to the next index
    5. if you finish iteration without finding anything, return false
    6. if you find the duplicate return true
    """
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for i in range(len(nums)):
            if nums[i] in nums_set:
                return True
            nums_set.add(nums[i])
        return False
         