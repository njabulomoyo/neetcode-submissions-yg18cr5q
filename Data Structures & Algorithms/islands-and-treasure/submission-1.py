class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        Rows, Cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def dfs(r,c):
            if (r<0 or c<0 or r==Rows or
                c==Cols or (r,c) in visited or
                grid[r][c] == -1):
                return 

            visited.add((r,c))
            q.append((r,c))


        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append((r,c))
        distance=0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = distance

                dfs(row+1, col)
                dfs(row-1, col)
                dfs(row, col+1)
                dfs(row, col-1)
            distance += 1

