class Solution:
    """
    input - list
    output - list of indices that give target
    is the list sorted? No
    answer always be there/
    time? o(n) and space? o(n) 
    exmpty list? No
    solution:


    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numd = {}
        for indx, elem in enumerate(nums):
            diff = target - elem
            if diff in numd:
                return [numd[diff],indx]
            numd[elem] = indx
            