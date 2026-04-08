class Solution:
    """
    understand:
    -  the input array is sorted
    - are we guaranteed of finding the two numbers that add up to the target?
    - output = two indices in a list
    - what is the best time and space complexity? 0(n) time and O(1) space
    - should the indices be listed in any order?

    Match:
    we will use two points

    plan:
    - since the list is sorted we will use two pointers to search the indices with the numbers
    - if we find that the numbers on the indices total to a number smaller than the target, we move the left index by one
    - if the numbers is bigger, we move the right index
    - move till we find the solution
    - the solution has to be one indexed

    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1

             

        



