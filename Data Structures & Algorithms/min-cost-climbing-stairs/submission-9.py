class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = [0] * len(cost)
        def dfs(i):
            if i >= len(cost):
                return 0
            if res[i] != 0:
                return res[i]

            res[i] = cost[i] + min(dfs(i+1), dfs(i+2))

            return res[i]

        return min(dfs(0), dfs(1))