class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        islands=0

        def checkConnection(r,c):
            if (r<0 or c<0 or r==Rows or
                c==Cols or grid[r][c]!="1"):
                return 0
            grid[r][c] = "0"
            for dr, dc in directions:
                checkConnection(r+dr, c+dc)


        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == "1":
                    checkConnection(r,c)
                    islands += 1

        return islands