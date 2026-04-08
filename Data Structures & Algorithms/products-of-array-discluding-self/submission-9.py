class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1,1,2,8
        #[1,2,4,6]
        #[48,24,6,1]
        res = [1]*len(nums)
        prod = 1
        for i in range(len(nums)):            
            res[i] = prod
            prod *= nums[i]
        print(res)
        res2 = [1]*len(nums)
        prod2 = 1

        for j in range(len(nums)-1,-1,-1):
            res2[j] = prod2
            prod2 *= nums[j]
        print(res2)

        for a in range(len(nums)):
            res[a] *= res2[a]

        return res 



