class Solution:
    """
    output - list (possible combinations that give the target)
    is the list sorted? no
    duplicates? yes we need to find a system of skipping over duplicates. if we have duplicates we a chance of doing the same iterations more than once
    need to sort the list to group our duplicates

    PlAN
        1. Get three pointers
        2. first one will iterate through the whole list
        3. the other two, one will be next to the first one and the other will be at the end
        4. the other two will be for finding all combinations that add up to the target that start with the number on the first pointer
        5. we'll do this for all the numbers
        6. we need a result list where we will be appending our combinations
        7. we also need to sort the list


    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for ind, val in enumerate(nums):
            if ind > 0 and val == nums[ind-1]:
                continue

            l, r = ind + 1, len(nums) -1
            while l < r:
                target = val + nums[l] + nums[r]
                if target < 0:
                    l += 1
                elif target > 0:
                    r -= 1
                else:
                    res.append([val,nums[l],nums[r]])
                    l += 1
                    r -= 1

                    while l<r and nums[l] == nums[l-1]:
                        l += 1

        return res 




















        