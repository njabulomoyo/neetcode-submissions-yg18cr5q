class Solution:
    """
    input: list
    output: int
    edge cases? duplicates? if we encounter duplicates, continue
    Solution:
    - sort the list
    - initiate var for keeping max count so far
    - initiate var for counting seq each time there are consequtive
    - iterate thru sorted list keepig count of the max seq found
    - return max sequence
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        snums = set(nums)
        nums = list(snums)

        for ind, val in enumerate(nums):
            if val-1 in snums:
                continue
            if val-1 not in snums:
                i = 0
                count = 0 
                while val + i in snums:
                    i+= 1
                    count += 1
                res = max(count,res)

        return res










        