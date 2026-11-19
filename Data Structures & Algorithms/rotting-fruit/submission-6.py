class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        q = deque()
        freshFruits = 0
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    freshFruits += 1

        time = 0
        while freshFruits and q:
            for _ in range(len(q)):
                
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if (nr<0 or nc<0 or nr==Rows or
                        nc==Cols or grid[nr][nc]!=1):
                        continue

                    freshFruits -= 1
                    grid[nr][nc] = 2
                    q.append((nr,nc))
            time +=1


                    

        return time if freshFruits==0 else -1
             







        