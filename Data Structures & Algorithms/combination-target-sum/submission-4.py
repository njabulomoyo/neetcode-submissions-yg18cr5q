class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sublist = []
        def dfs(i, total):
            if total > target or i == len(nums):
                return 
            if total == target:
                res.append(sublist.copy())
                return 
            total += nums[i]
            sublist.append(nums[i])
            dfs(i, total)

            total -= nums[i]
            sublist.pop()
            dfs(i+1, total)

        dfs(0,0)
        return res


            