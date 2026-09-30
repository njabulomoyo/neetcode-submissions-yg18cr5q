class Solution:
    """
    output: int minutes it takes to affect all the oranges
    brainstorm:
    - check out all the rotten fruits
    - also chec the total number of fresh fruits
    - add them to a queue, 
    - for each round of iteration, add to time
    - do this until all the rotten fruits are done
    - or untile there is nothing of the queue


    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])

        q = deque()
        freshfruit = 0

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    freshfruit += 1

        def rotten(r,c):
            nonlocal freshfruit
            if (r<0 or c<0 or r==Rows or 
                c==Cols or grid[r][c] != 1):
                return 

            grid[r][c] = 2
            q.append((r,c))
            freshfruit -= 1



        minutes = 0
        while q and freshfruit:
            for _ in range(len(q)):
                row, col = q.popleft()

                rotten(row+1, col)
                rotten(row-1, col)
                rotten(row, col+1)
                rotten(row, col-1)

            minutes += 1

        return minutes if freshfruit == 0 else -1
