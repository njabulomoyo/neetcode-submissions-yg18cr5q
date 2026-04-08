class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1 #l=3, r=3
        while l<=r:
            mid = (l+r)//2 #3
            if nums[mid]==target:
                return mid
            elif nums[mid] > target:
                r = mid - 1#3
            else:
                l = mid + 1#3
        return -1

        #
        