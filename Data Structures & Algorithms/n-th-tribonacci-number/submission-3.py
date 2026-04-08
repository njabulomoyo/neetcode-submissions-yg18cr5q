class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n == 2:
            return 1
        dp = {}
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        def helper(x):
            for i in range(n-2):
                if x in dp:
                    return dp[x]

                else:
                    dp[x] = helper(x-1) + helper(x-2) + helper(x-3)
                    return dp[x]
            
        return helper(n)


        """
        if n == 0: return 0
        if n == 1 or n == 2:
            return 1
        a = 0
        b = c = 1
        for i in range(n-2):
            tempC,tempB = c, b
            c += b + a
            b = tempC
            a = tempB

        return c
        """

