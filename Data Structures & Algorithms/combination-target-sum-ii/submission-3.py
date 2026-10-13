class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        total=0
        res = []
        sublist = []
        candidates.sort()
        def dfs(i):
            nonlocal total
            if total == target:
                res.append(sublist.copy())
                return 
            if total > target or i == len(candidates):
                return
            

            total += candidates[i]
            sublist.append(candidates[i])

            dfs(i+1)
            total -= candidates[i]
            sublist.pop()

            while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
                i+= 1

            dfs(i+1)

        dfs(0)
        return res

        