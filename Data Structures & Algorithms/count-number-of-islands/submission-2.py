class Solution:
    def  numIslands(self, grid: List [List[str]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def check_neighbors(r, c):
            if (r<0 or c<0 or r==Rows or c==Cols or
                grid[r][c] != "1" or (r,c) in visited):
                return
            visited.add((r,c))
            check_neighbors(r+1,c)
            check_neighbors(r-1,c)
            check_neighbors(r,c+1)
            check_neighbors(r,c-1)
  	

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    check_neighbors(r, c)
                    
                    islands += 1
        return islands

        