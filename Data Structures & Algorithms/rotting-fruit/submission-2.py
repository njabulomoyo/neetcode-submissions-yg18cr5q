class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        q = deque()
    
        def rotten(r,c):
            nonlocal oranges
            if (r<0 or c < 0 or r == Rows or 
                c==Cols or grid[r][c] != 1):
                return 
            oranges -= 1
            q.append((r,c))
            grid[r][c] = 2
            
        oranges = 0
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    oranges += 1
                

        count = 0
        while oranges > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                rotten(r+1, c)
                rotten(r-1, c)
                rotten(r, c+1)
                rotten(r, c-1)
                         
            count += 1

        return count if oranges == 0 else -1






    

