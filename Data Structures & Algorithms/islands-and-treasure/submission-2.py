class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        Rows, Cols = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        q = deque()
        visited = set()

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        dist = 0     
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if (nr<0 or nc<0 or nr==Rows or
                        nc==Cols or (nr,nc) in visited or
                        grid[nr][nc]==-1):
                        continue

                    q.append((nr,nc))
                    visited.add((nr,nc))

            dist += 1



        
