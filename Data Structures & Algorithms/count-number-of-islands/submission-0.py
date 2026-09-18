class Solution:
    """
    - there is iteration thru the elements on the list
    - check all the neighboring elements on the grid, condition should check if the elem is equal to 1, check if the indices are not out of range, the row and the column, check if the elem has been visited
    - should initiate set for storing visited elems, variable for keeping count of the number of islands
    - VARS FOR length of row and length of column

    """
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        Rows, Cols = len(grid), len(grid[0])
        
        if not grid:
            return 0
        island = 0

        def dfs(r,c):
            if (r < 0 or c < 0 or
                r >= Rows or c >= Cols or
                grid[r][c] != "1"):
                return 

            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    island += 1

        return island
