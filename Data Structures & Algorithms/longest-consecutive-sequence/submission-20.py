class Solution:
    """
    output: int
    breakdown: for the sequesnces, find the longest
    output: int

    Brainstorm:
    -input- unsorted list
    -can it be empty? 
    -range of nums on list? 0 <=
    -duplicates? skip duplicates

    -solution:
    sort the list
    iterate thru
    keep a count var

    - convert list to set
    - iterate thru set
    - for each num, check is beginning of seq, 
    - if true, start count
    - record longest seq so far
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in numSet: 
            if (num-1) not in numSet:
                count = 0
                i=0
                while num+i in numSet:
                    count += 1
                    i += 1
                res = max(res, count)

        return res

                











        