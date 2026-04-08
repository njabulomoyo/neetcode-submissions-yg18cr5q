class Solution:
    """
    - understand:
    - input is a list
    - expected time complexity is O(logn)
    - output should be an index of the target and if it is not present, return -1

    match:
    - linear search, using iterations -> O(n)
    - binary search, -> O(logn)

    Plan/design:
    1. have a left, right and mid pointer
    2. using the mid pointer, check if the number is equal to the target
    3. if not, compare the last element on the rotated list with the target.
    4. if it's greater than the mid point, then it means target is on the right side the mid point, and the left side isnt.
    5. 


    """
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1 #l, r = 4, 6
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1 
    

        