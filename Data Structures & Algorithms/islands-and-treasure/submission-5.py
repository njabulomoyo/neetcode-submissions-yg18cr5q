class Solution:
    """
    find all the treasure chests and the start counting from there,
    till we finish all land that is reachable.
    we add all the treasures to a queue
    then we update the neighbors around the same time


    2d grid,
    land that cannot the traversed
    """
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        Rows, Cols = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        INF = 2147483647
        #find all the treasures
        q = deque()
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        #function for populating the neighbors
        distance = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if (nr<0 or nc<0 or nr==Rows or
                        nc==Cols or grid[nr][nc]!=INF):
                        continue
                    grid[nr][nc] = grid[row][col] + 1
                    q.append((nr,nc))

            
                    










        