class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums ==[]:
            return 0
        
        numSet = set(nums)
        longest = 0
        for elem in numSet:
            count = 0
            if (elem - 1) not in numSet:
                i = 0
                while (elem + i) in numSet:
                    count += 1
                    i += 1
                longest = max(count, longest)
        
        return longest

        