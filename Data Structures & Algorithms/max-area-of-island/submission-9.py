class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        maxArea = 0

        def bsf(r,c):
            nonlocal area
            q.append((r,c))
            grid[r][c] = 0
            area += 1

            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    for dr, dc in directions:
                        nr,nc = row+dr, col+dc
                        if (nr<0 or nc<0 or nr==Rows or
                            nc==Cols or grid[nr][nc] == 0):
                            continue
                        q.append((nr,nc))
                        grid[nr][nc] = 0
                        area += 1

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 1:
                    area = 0
                    bsf(r,c)
                    maxArea = max(maxArea, area)

        return maxArea