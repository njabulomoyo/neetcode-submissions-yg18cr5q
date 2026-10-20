class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        q = deque()
        fresh = 0
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        minutes=0 
        while q and fresh:
            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nc<0 or nr<0 or nr==Rows or 
                        nc==Cols or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    q.append((nr,nc))
                    fresh -= 1
            minutes += 1

        
        return minutes if fresh==0 else -1
