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
        print(res1)
        prod = 1
        #[1,1,2,8]
        for i in range(len(nums)-1,-1,-1):
            res1[i] *= prod 
            prod *= nums[i]
        
        return res1 



            