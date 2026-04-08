class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre = 1   #[1,2,3,4]
        for i in range(len(nums)):#i=3
           res[i],pre = pre, pre * nums[i]# 
        #[1,1,2,6]
        #pre = 4*6 = 24 
        #[1,2,3,4]
        post = 1
        for i in range(len(nums)-1, -1,-1):#0
         
            res[i] *= post#[24,12,8,6]
            print(res)
            post *= nums[i]#post = 24
            
        
        return res

        
        