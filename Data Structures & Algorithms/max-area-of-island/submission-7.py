class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()
        maxArea = 0

        def dfs(r,c):
            nonlocal total
            if (r<0 or c<0 or r==Rows or
                c==Cols or grid[r][c]!=1):
                return 

            grid[r][c] = 0
            total += 1
            for dr, dc in directions:
                dfs(r+dr, c+dc)


        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 1:
                    total=0
                    dfs(r,c)
                    maxArea = max(maxArea, total)

        return maxArea


