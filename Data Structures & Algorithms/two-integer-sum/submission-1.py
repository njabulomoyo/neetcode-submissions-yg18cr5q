class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict_nums:
                return [dict_nums[diff],i]  
            dict_nums[nums[i]] = i
        
        return []



        