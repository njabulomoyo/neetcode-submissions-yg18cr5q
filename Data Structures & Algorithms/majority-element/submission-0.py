class Solution:
    """
    input - list
    output - the majority element
    edge cases? empty list? 
    time o(n) and space o(1) complexity?

    MATCH:
    - Iterate
    - hashmaps

    PLAN:
    1. keep count of the occurence of each element we are at
    2. keep track of the element 
    3. iterate thru list
    4. 

    """
    
    def majorityElement(self, nums: List[int]) -> int:
        freq = 0 
        res = None

        for i in nums:
            if freq == 0:
                res = i
                freq += 1
            elif res == i:
                freq += 1
            else:
                freq -= 1

        return res











        