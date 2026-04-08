class Solution:
    """
    understand:
    what is meant by consecutive sequence? [1,2,3,4]
    edge cases? empty string? return 0 all unique numbers? return 1
    expected time 0(n) and space o(n)?
    will there be any duplicates
    MATCH:
    -hashmap
    -iteration
    PLAN:
    -iterate through the elements
    -check if element is start of a sequence?
    -if yes, continue checking till you find length
    - if no, continue
    [1,1,2,3,4,5,6]
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set(nums)
        nums = list(numSet)
        i=0
        while i < len(nums):
            if (nums[i]-1) in numSet:
                i+=1
                continue
            else:
                j = count = 0
                while (nums[i]+j) in numSet:
                    count += 1
                    j += 1
                res = max(res,count)
            i += 1
        
        return res
            




        