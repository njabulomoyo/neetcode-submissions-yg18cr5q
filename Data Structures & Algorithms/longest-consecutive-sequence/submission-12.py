class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        i = 0
        numSet = set(nums)
        nums = list(numSet)
        while i < len(nums):
            if not (nums[i]-1) in numSet:
                j = 0
                count = 0
                while nums[i]+j in numSet:
                    count += 1
                    j+=1
                i += j
                res = max(res,count)
            else:
                i += 1

        return res
            
                