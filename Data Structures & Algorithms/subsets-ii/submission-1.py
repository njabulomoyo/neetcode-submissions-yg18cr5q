class Solution:
    """
    output: list of list
    edge case: if there are duplicates?

    Solution:
    - using a recursive solution
    - sort the list
    - inititate sublist and result list
    - have two recursive calls, one with the elem i added and another without the element
    - before the second recursive call, skip duplicates
    - if i == len(nums), add sublist to the result list
    - if 
    """
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sublst = []
        nums.sort()
        def dfs(i):
            if i == len(nums):
                res.append(sublst.copy())
                return 
            sublst.append(nums[i])
            dfs(i+1)

            sublst.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)
        dfs(0)
        return res




        