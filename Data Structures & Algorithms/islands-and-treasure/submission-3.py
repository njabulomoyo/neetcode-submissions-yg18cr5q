class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        Rows, Cols = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        dist = 0
        visited = set()
        q = deque()
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if (nc<0 or nr<0 or nr==Rows or 
                        nc==Cols or grid[nr][nc]==-1 or 
                        (nr,nc) in visited):
                        continue
                    visited.add((nr,nc))
                    q.append((nr,nc))
            dist += 1



