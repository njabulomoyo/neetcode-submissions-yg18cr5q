class Solution:
    """
    output: list of list (all subsets)

    solution:
    - recursive solution
    - initiate result list and subset list (modified at every recursive call)
    - we'll process evry elem in list
    - for each elem at index i, we'll have two recursive calls, either include the elem or not
    - do this until i == len(nums)
    - return the result list
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sublst = []

        def dfs(i):
            if i == len(nums):
                res.append(sublst.copy())
                return
            sublst.append(nums[i])
            dfs(i+1)

            sublst.pop()
            dfs(i+1)
        dfs(0)
        return res

