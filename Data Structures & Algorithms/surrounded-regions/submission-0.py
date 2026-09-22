class Solution:
    """
    - Start by getting all the regions that are at the borders,
    put them in a list/queue
    - then from those regions, we will chck the rest of the regions and that are connected to those at the border
    - we put those regions in a set
    - we then go over the whole thing the grid, those regions not on the set, we convert them to encosed cells
    - done!
    - 
    """
    def solve(self, board: List[List[str]]) -> None:
        Rows, Cols = len(board), len(board[0])
        visited = set()
        NotSurrounded = set()
        #q = deque()

        def dfs(r,c, visited, NotSurrounded):
            if (r<0 or c<0 or c == Cols or
                r == Rows or (r,c) in visited or 
                board[r][c]=="X"):
                return 
            visited.add((r,c))
            NotSurrounded.add((r,c))
            dfs(r+1, c, visited, NotSurrounded)
            dfs(r-1, c, visited, NotSurrounded)
            dfs(r, c+1, visited, NotSurrounded)
            dfs(r, c-1, visited, NotSurrounded)

        for r in range(Rows):
            if board[r][0] == "O":
                dfs(r, 0, visited, NotSurrounded)
            if board[r][Cols-1] == "O":
                dfs(r, Cols-1, visited, NotSurrounded)

        for c in range(Cols):
            if board[0][c] == "O":
                dfs(0, c, visited, NotSurrounded)
            if board[Rows-1][c] == "O":
                dfs(Rows-1, c, visited, NotSurrounded)



        for r in range(Rows):
            for c in range(Cols):
                if (r,c) not in NotSurrounded:
                    board[r][c] = "X"

        








            

        