class Solution:
    """
    understand:
        - input - int
        - output - int
        base case: n == 0: return 0

    """
    def climbStairs(self, n: int) -> int:
        cur = prev = 1

        for i in range(n-1):
            temp = cur
            cur = cur + prev
            prev = temp

        return cur

        if n < 0: return 0
        if n == 0: return 1
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)

