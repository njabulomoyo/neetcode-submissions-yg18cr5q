class Solution:
    """
    output: int mx number of islands
    brainstorm:
    - look for all connected islands
    - initiate hash set to store visited elements
    - count how many they are
    - keep track of the max
    - iterate thru the whole grid to check all the islands
    - dfs recursion
    - return the max num island
    """


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        visited = set()
        res = 0
        def dfs(r, c):
            nonlocal count
            if (r < 0 or c < 0 or r == Rows or c == Cols or 
             grid[r][c] != 1):
                return 

            grid[r][c] = 0
            count += 1
            dfs(r+1, c, )
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        
        for r in range(Rows):
            for c in range(Cols):                
                if grid[r][c] == 1:
                    count=0
                    dfs(r, c)
                    res = max(res, count)
                    
                    
                    

                    
        return res


