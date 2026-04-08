class Solution:
    """
    output - int (highest freq)
    edge cases:
    - empty list? return []
    - duplicates? remove duplicates, convert the whole thing into a set

    Solution:
    - iterate thru the numbers
    - initiate counter var
    - check if the number is the start of a list or not
    - if true, start counting, we'll keep the count
    - compare with current max
    - if false: continue
    - do this till the end of the list
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        nums = list(numSet)
        count = 0

        for num in nums:
            if (num-1) not in numSet:
                i = 0
                cnt = 0
                while (num + i) in numSet:
                    cnt += 1
                    i += 1
                count = max(cnt, count)

        return count











        