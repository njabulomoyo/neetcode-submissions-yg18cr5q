class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        sublst = []
        def dfs(i, total):
            if total == target:
                res.append(sublst.copy())
                return 
            if total > target or i == len(candidates):
                return 


            total += candidates[i]
            sublst.append(candidates[i])
           
            dfs(i+1, total)
            
            total -= candidates[i]
            sublst.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, total)

        dfs(0, 0)
        return res
        