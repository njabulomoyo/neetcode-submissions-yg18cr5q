class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1 #l=2, r=2
        while l<=r:
            mid = (l+r)//2 #2
            if nums[mid] < nums[r]:
                r = mid #r=2
            else:
                l = mid + 1#l=2
        return nums[r]
            


        