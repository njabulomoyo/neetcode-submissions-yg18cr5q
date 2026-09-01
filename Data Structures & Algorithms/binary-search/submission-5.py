class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #initiate pointers l and r, one at the beginning and another at the end
        l, r = 0, len(nums)-1

        #calculate midpoint
        while l <= r:
            m = (l + r)// 2
        # check if midpoint is equal to the target
            if nums[m] == target:
                return m

        # if greater, move l to the right of midpoint
            elif nums[m] < target:
                l = m+1

        # else, move r to the left of midpoint
            else:
                r = m - 1

        #continue until target is found. return -1 if not found
        return -1
        