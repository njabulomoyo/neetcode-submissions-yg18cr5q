class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for indx,a in enumerate(nums):
            if indx != 0 and nums[indx-1] == a:
                continue
            l,r = indx+1,len(nums)-1
            while l < r:
                sum = nums[l]+nums[r]+a
                if sum < 0:
                    l+=1
                elif sum > 0:
                    r-=1 
                else:
                    res.append([nums[l],nums[r],a])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                        continue

        return res