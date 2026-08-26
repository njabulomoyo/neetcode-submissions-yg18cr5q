class Solution:
    """
    output: subarray
     edge cases: list cant be empty, 

    Solution:
    initiate two pointers, l and r
    figure out when to move them
    """
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        sumArr = 0
        for num in nums:
            if sumArr < 0:
                sumArr = 0

            sumArr += num
            maxSub = max(maxSub, sumArr)

        return maxSub

