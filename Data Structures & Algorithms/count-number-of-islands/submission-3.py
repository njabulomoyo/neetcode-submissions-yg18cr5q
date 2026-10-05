class Solution:
    from collections import deque
    def  numIslands(self, grid: List [ List [ str ]]) -> int:
        if not grid:
            return 
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        Rows, Cols = len(grid), len(grid[0])
        q = deque()  	
        islands = 0
        def bfs(r,c): 
            q.append((r,c))
            grid[r][c] == "0"

            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    for r, c in directions:
                        nr, nc = row+r, col+c
                        if (nr<0 or nc<0 or nr==Rows or
                            nc==Cols or grid[nr][nc] != "1"):
                            continue

                        q.append((nr,nc))
                        grid[nr][nc] = "0"
                        

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1

        return islands
