class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sublst = []
        def dfs(opend, closed):
            if opend == closed == n:
                res.append("".join(sublst))

            if opend < n:
                sublst.append("(")
                dfs(opend+1, closed)
                sublst.pop()

            if closed < opend:
                sublst.append(")")
                dfs(opend, closed+1)
                sublst.pop()

        dfs(0,0)
        return res

