class Solution:
    """
    understand:
    input - list of int
    output - lst without val
    edge cases? emepty list return empty list
    expected time o(n) and space o(n) complexity 

    MATCH:
    - iterate
    - list

    PLAN:
    1. Create new list
    2. iterate thru
    3. find elements that are not equal to val
    4. send them to the front
    5. keep track of the indice you're at

    """
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 
        for elem in nums:
            if elem != val:
                nums[i] = elem
                i += 1
        return i
            

        
        