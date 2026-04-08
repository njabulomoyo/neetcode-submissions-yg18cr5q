class Solution:
    """
    understand:
    input - list
    output - list
    edge cases:
        - empty list?
        - 
    Match:
        - lists and iteration
    
    plan:
    1. iterate through the list once, find the products,
    to the right of the indices
    2. iterate through the list backwards, find the products,
    to the left of the indices
    3. return the result of the product of the two lists combined

    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums) 
        prod = 1
        for i in range(len(nums)):
            res[i] = prod
            prod *= nums[i]
        prod = 1
        print("res is ",res)
        for i in range(len(nums)-1,-1,-1):
            res[i] *= prod
            prod *= nums[i]

        return res





        