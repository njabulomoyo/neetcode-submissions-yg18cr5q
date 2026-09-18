class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        Rows, Cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def addRoom(r,c):
            if (r <0 or c <0 or r == Rows or
                c == Cols or grid[r][c] == -1 or
                (r,c) in visited):
                return 
            visited.add((r,c))
            q.append((r,c))


        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
            dist += 1










