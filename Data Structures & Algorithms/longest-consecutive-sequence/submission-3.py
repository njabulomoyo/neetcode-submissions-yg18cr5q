class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        highest, count = 0, 1
        #[0,2,6,7,8]
        for i in range(1,len(nums)): # i = 4
            if nums[i] - nums[i-1] == 1: #nums[i]=8, nums[i-1] = 7
                count += 1 #count=3 
            else:
                highest = max(highest, count)# hst= 1, count=1...hst=1
                count = 1
        highest = max(highest, count)
        return highest
        




        