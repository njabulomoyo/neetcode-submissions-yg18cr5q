class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1]*len(nums)
        for i in range(len(nums)-1):
            res = 1
            for j in range(i+1, len(nums)):
                res *= nums[j]
            result[i] = res
  
        for i in range(len(nums)-1,0,-1):
            res = 1 
            for j in range(i-1,-1,-1):
  
                res *= nums[j]
                print("res:",res)
            result[i] *= res

        return result

