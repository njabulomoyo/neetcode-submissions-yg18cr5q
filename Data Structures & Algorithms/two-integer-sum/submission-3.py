class Solution:
    """
    understand:
    - answer always there?
    - empty input list?
    - what is the expected time and space complexity?
    match:
        - dictionary
    plan:
    - iterate through the list
    - initialize a dictionary to store all the values we have passed through
    - for every current number on the list we will subtract it from the target to get diff
    - as we are iterating, we will be looking for diff inside our dictionary    
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {} 
        for indx, elem in enumerate(nums): 
            diff = target - elem 
            if diff in d: 
                return [d[diff],indx]
            d[elem] = indx 












        