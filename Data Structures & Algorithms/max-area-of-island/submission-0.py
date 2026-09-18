class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        Rows, Cols = len(grid), len(grid[0])
        mxm = 0

        def dfs(r,c):
            nonlocal island
            if (r < 0 or c < 0 or
                r >= Rows or c >= Cols or
                grid[r][c] != 1):
                return 

            grid[r][c] = 0
            island += 1
            for dr, dc in directions:
                dfs(r+dr, c+dc)
            

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 1:
                    island = 0
                    dfs(r,c)
                    print("island is", island)
                    mxm = max(island, mxm)

        return mxm