class Solution:
    """
    understanding:
        input - list
        output - list

    plan:
    1. ite
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod =  1
        res1 = [1]*len(nums)
        for i in range(len(nums)):
            res1[i] = prod
            prod *= nums[i]

        res2 = [1] * len(nums)
        prod = 1
        for i in range(len(nums)-1,-1,-1):
            res2[i] = prod 
            prod *= nums[i]

        for j in range(len(nums)):
            res1[j] *= res2[j]

        return res1 



            