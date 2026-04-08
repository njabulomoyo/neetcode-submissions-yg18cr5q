class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums) 
        for i in range(len(nums)): #i=1
            for j in range(i+1,len(nums)): #j=3
                res[i] *= nums[j]
        print(res)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i-1,-1,-1):
                res[i] *= nums[j]
        
        return res