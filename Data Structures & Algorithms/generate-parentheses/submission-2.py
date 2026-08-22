class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sublst = []

        def dfs(openN, closeN):
            if openN == closeN == n:
                res.append("".join(sublst.copy()))
                return 

            if openN < n:
                sublst.append("(")
                dfs(openN+1, closeN)
                sublst.pop()

            if openN > closeN:
                sublst.append(')')
                dfs(openN, closeN+1)
                sublst.pop()

        dfs(0,0)

        return res
        