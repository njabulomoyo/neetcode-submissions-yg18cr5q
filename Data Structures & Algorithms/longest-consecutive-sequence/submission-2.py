class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        highest, count = 0, 1

        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                count += 1
            else:
                highest = max(highest, count)
                count = 1
        highest = max(highest, count)
        return highest
        




        