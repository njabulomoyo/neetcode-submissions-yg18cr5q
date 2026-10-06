class Solution:
    """
    output: int(target index)

    find the target on the given list
    brainstorm:
    - list is sorted, 
    - we can implement binary search
    - set two pointers one at the start and another at the end
    -check midpoint, check if equal to target
    - check if less, move left pointer
    - check if more, move right pointer
    - continue till the l>=r
    - if target not found return -1
    """
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m-1
            else:
                l = m+1

        return -1
        