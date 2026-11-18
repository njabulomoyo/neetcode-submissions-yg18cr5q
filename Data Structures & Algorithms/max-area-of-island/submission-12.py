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
            q=deque()
            q.append((r,c))
            grid[r][c] = 0

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if (nr<0 or nc<0 or nr==Rows or
                        nc==Cols or grid[nr][nc]!= 1):
                        continue
                    total += 1
                    grid[nr][nc] = 0
                    q.append((nr,nc))

        maxArea = 0
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 1:
                    total = 1
                    checkNeighbors(r,c)
                    maxArea = max(maxArea, total)

        return maxArea
        