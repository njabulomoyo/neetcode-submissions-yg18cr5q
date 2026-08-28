class Solution:
    """
    output: int (number of subarrays that meet the requirements)

    edge cases? no empty lst

    Solution:
    - initiate two pointers l and r
    conditions for moving pointers:
    - move r on each iteration 
    - checking if subarray meets requirement
    - move l each time, check individual numbers if they meet standard
    """   
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        prod = 1
        for r in range(len(nums)):
            prod *= nums[r]
            while l <= r and prod >= k:
                prod //= nums[l]
                l += 1
            res += (r-l + 1)
        return res
            




