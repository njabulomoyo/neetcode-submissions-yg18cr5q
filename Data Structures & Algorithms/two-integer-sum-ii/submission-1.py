class Solution:
    """
    understand:
    -  the input array is sorted
    - are we guaranteed of finding the two numbers that add up to the target?
    - output = two indices in a list
    - what is the best time and space complexity? 0(n) time and O(1) space

    Match:
    we will use two points

    plan:
    - since the list is sorted we will use two pointers to search the indices with the numbers
    - if we find that the numbers on the indices total to a number smaller than the target, we move the left index by one
    - if the numbers is bigger, we move the right index
    - move till we find the solution

    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]


