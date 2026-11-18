class Solution:
    """
    find the islands, check neighbors
    each found neighbor, add to the count,
    count all neigbors, get total area for those connected blocks
    move thru the other islands in the grid
    keep track of max area
    """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,-1], [0,1]]

        def checkNeighbors(r,c):
            nonlocal total
            if (r<0 or c<0 or r==Rows or 
                c==Cols or grid[r][c] == 0):
                return 

            grid[r][c] = 0
            total += 1
            for dr, dc in directions:
                checkNeighbors(r+dr, c+dc)

            

        maxArea = 0
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 1:
                    total = 0
                    checkNeighbors(r,c)
                    maxArea = max(maxArea, total)

        return maxArea
        