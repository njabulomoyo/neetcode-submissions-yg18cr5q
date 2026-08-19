class Solution:
    """
    output: [list of the indices giving the total]
    edge cases: 
    -list cant be empty
    -

    solution:
    - initiate a set for storing all the elems passed
    - iterate thru the list
    - for each elem, find the diff between the curr and target.
    - then check if the diff exists in the dict
    - should store the indx of the elem as well
    - do this till you find the indices

    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict()

        for indx, val in enumerate(nums):
            diff = target - val
            if diff in d:
                return [d[diff],indx]

            d[val] = indx
        