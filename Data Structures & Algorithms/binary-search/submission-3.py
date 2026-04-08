class Solution:
    """
    understand:
    - input - list
    - output - index of the target
    edge cases - empty?
    if target is not there, return -1
    matching:
        - binary search
        - two pointers
    planing:
    1. spit the list into two.
    2. check if the middle value is the target or if
    if greater or less tha the target
    3. if its less, the move the left point one point left of the middle point
    4. if its more, move the right pointer to the one point right of the middle point.
    5. continue process till you find target
    6. if target is found, return index
    7. otherwise, return -1

    implement:
    evaluate:


    """
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1 
        return -1



        