class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        res = 1
        for i in range(len(nums)):
            result[i]=res
            res *= nums[i]
 
        res = 1 
        for i in range(len(nums)-1,-1,-1):                
            result[i] *= res
            res *= nums[i]

        return result

