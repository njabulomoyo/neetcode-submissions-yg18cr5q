class Solution:
    """
    understand:
    the list is already sorted
    target might not be there
    the output should be index of the target
    expected time is O(log n)

    plan:
    have a mid, left and right pointer 
    the left pointer == 0, right pointer == len-1 
    check if the mid pointer is the target
    if nums[mid] less than the target, move left to mid+1
    if nums[mid] is greater than target, move right to mid - 1
    if the target is not there, return -1

    """
    def search(self, nums: List[int], target: int) -> int:
        #[-1,0,2,4,6,8]
        l, r = 0, len(nums)-1 #l = 3, r= 3
        while l<= r:
            mid = (l+r)//2 # m=3 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1 #l=3
            else:
                r = mid - 1 #r=3
        return -1