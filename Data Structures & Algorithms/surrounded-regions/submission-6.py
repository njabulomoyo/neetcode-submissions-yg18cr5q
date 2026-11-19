class Solution:
    def solve(self, board: List[List[str]]) -> None:
        Rows, Cols = len(board), len(board[0])
        directions = [[1,0],[-1,0],[0,-1],[0,1]]

        def checkNeighbor(r,c):
            if (r<0 or c<0 or r==Rows or
                c==Cols or board[r][c] != "O"):
                return 

            board[r][c] = "Z"
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                checkNeighbor(nr,nc)

        for r in range(Rows):
            checkNeighbor(r,0)
            checkNeighbor(r,Cols-1)

        for c in range(Cols):
            checkNeighbor(0, c)
            checkNeighbor(Rows-1,c)

        for r in range(Rows):
            for c in range(Cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "Z":
                    board[r][c] = "O"




