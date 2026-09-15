class Solution:
    """
    output: list of list

    edge cases? alll elements are distict

    Solution:
    - var, result list, sum of sublist, sublist
    - recursive solution
    - 
    """
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sublst = []
        total = 0 
        def dfs(i):
            nonlocal total, res, sublst

            if total > target or i == len(nums):
                return 
            if total == target:
                res.append(sublst.copy())
                return

            total += nums[i]
            sublst.append(nums[i])
            dfs(i)

            total -= nums[i]
            sublst.pop()
            dfs(i+1)

        dfs(0)
        return res

        