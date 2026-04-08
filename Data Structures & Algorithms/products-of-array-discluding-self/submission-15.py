class Solution:
    """
    output - list
    solution:
    bruteforce:
    - for each num, multiply by every other number on the list
    - do it from start to finish and then from finish to start
    - then add the products of both lists
    - divide the products by the original numbers on the list

    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = [1]*len(nums)

        for i in range(len(nums)-1):            
            for j in range(i+1,len(nums)):
                lst[i] *= nums[j]

        for i in range(len(nums)-1, 0, -1):
            for j in range(i-1, -1, -1):
                lst[i] *= nums[j]

        return lst





