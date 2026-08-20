class Solution:
    """
    output: int longest sequence

    edge cases: empty list? return 0, duplicates? remove duplicates

    solution:
    - initiate a pointer to iterate thru list
    - create set to store list elems
    - for each elem, check if its the beginning of seq or not:
      * if elem-1 exists in the set (elem not start of seq), opposite is true
    - once find start of a seq, check seq but add one to elem and checking if number exists in set
    - do this till find no number
    - count as you add
    - keep track of the longest seq
    return result

    """
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)
        newNums = list(numSet)
        res = 0 
        for ind, val in enumerate(newNums):
            if val-1 not in numSet:
                count = 0
                i = 0
                while (val + i) in numSet:
                    count += 1
                    i += 1

                res = max(count, res)

        return res








        