class Solution:
    """
    output: int - index of the target
    edge cases? empty list, no empty list, if no target, return -1

    Solution: 
    - initiate two pointers, l and r
    - find midpoint
    - using midpoint and right pointers, check which side is sorted
    - if midpoint is less than r, then right side is sorted
    - check if target is on the sorted side or not
    continue checking until l => r
    """
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            m = (l + r)//2
            if nums[m] == target:
                return m

            if nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m - 1
            else:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

        return -1 


        