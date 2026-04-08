class Solution:
    """
    UMPIRE:
    Understand:
    find two numbers on the list that add up to the target number
    **inputs - list
    **output - list of the indices of the numbers that add up to the target number
    edge cases- 
        - are we guaranteed to find the numbers?
        - what if the list is empty?
        - is the list sorted?
        - will we have duplicates?

    Match:
    - if list is sorted - use binary search
    - dictionaries

    Plan:
    1. create dictionary 
    2. go through the whole list
    3. check if the difference (target - current element) exists on the dictionary?
    4. if it does, return the index of the current number and that of the difference on the dictionary
    5. otherwise, add the current number onto the dictionary, with its index
    6. continue till the end. 

    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictnums = {}
        for i in range(len(nums)):
            diff =  target -  nums[i]
            if diff in dictnums:
                return [dictnums[diff],i]
            dictnums[nums[i]] = i


        