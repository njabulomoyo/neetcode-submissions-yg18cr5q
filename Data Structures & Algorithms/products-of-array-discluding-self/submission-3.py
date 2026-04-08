class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        for i in range(len(nums)-1):
            prod = 1 
            for j in range(i+1,len(nums)):
                prod *= nums[j]
            res[i] = prod
        res[i+1] = 1
          
        #[48,24,6,1]

        for i in range(len(nums)-1,-1,-1):
            prod = 1
            for j in range(i-1,-1,-1):
                prod *= nums[j]
            res[i] = res[i] * prod

        return res

        #[1,1,2,8]


        