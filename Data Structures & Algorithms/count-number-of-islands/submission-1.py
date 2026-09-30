class Solution:
    """
    output: int number of islands

    iterate thru the grid
    find the island, then check neighbors to see any connecting islands
    after that we add to island
    do this for all the elements on the grid
    return thr num of island
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r,c):
            if (r < 0 or c < 0 or r == Rows or c == Cols 
               or grid[r][c] != "1"):
               return 

            grid[r][c] = 0
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)


        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1

        return islands

        