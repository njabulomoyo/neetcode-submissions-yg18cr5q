class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #{1,2,3,5,7}
        nums = set(nums)
        hst = count = 0
        for elem in nums: #elem = 1
            if elem-1 in nums:
                continue
            else:
                count=0
                i=0
                while elem + i in nums: #elem + i=0 => 5
                    count += 1 #count=1
                    i+=1 #i=1
            hst = max(hst,count) #count= 1, hst=3 => 3 
        return hst





        """
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
        """
        




        