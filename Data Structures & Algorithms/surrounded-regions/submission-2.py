class Solution:
    """
    output: modify the grid
    brainstorm
    - we iterate the elements on the edge 
    - then we check all then neighbors to see if they are are part of that region
    - traverse through the areas from the edge that are connected
    - all those regions will be put in a set
    -then we traverse thru the whole grid, looking for not visited, converting to "x"


    """
    def solve(self, board: List[List[str]]) -> None:
        Rows, Cols = len(board), len(board[0])
        visited = set()
        #helper function for checking neighbors
        def dfs(r,c, visited_set):
            if (r<0 or c<0 or r==Rows or
                c==Cols or (r,c) in visited or
                board[r][c] != "O"):
                return 

            visited_set.add((r,c))

            dfs(r+1,c,visited_set)
            dfs(r-1,c,visited_set)
            dfs(r,c+1,visited_set)
            dfs(r,c-1,visited_set)

        #iterating elements on the edges
        for r in range(Rows):
            if board[r][0] == "O":
                dfs(r, 0, visited)
            if board[r][Cols-1] == "O":
                dfs(r, Cols-1, visited)

        for c in range(Cols):
            if board[0][c] == "O":
                dfs(0, c, visited)
            if board[Rows-1][c] == "O":
                dfs(Rows-1, c, visited)

        for r in range(Rows):
            for c in range(Cols):
                if board[r][c]=="O" and (r,c) not in visited:
                    board[r][c] = "X"

            
        

        