class Solution:
    """
    understand:
    match:
        list

    Plan:
    create two lists
    iterate through list
    calculate products for numbers to the right of elements
    do same for numbers to the left of element
    combine the products of both lists

    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prod = 1
        for i in range(len(nums)):
            res[i] = prod
            prod *= nums[i]

        res2 = [1]*len(nums)
        prod2 = 1
        for j in range(len(nums)-1,-1,-1):
            res2[j] = prod2
            prod2 *= nums[j]
        print(res)
        print(res2)
        for a in range(len(nums)):
            res[a] *= res2[a]

        return res









