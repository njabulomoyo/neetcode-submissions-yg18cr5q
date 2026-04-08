class Solution:
    """
    understand:
        - input - list
        - output - int - longest sequence
    edge cases?
    - empty list?
    - will the list be sorted?
    - time complexity? o(n)
    - space o(n)
    match:
        - hashset
        - pointers
    plan:
    1. iterate through the list
    2. check if number is the start of a list?
    3. if it is, check the sequence
    4. if not continue
    5. keep record of the highest sequence

    """
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for i in nums_set:
            if (i-1) in nums_set:
                continue
            else:
                count = 0
                while (i+count) in nums_set:
                    count += 1
                    
                res = max(res,count)

        return res


        