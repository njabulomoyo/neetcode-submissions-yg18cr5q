class Solution:
    def solve(self, board: List[List[str]]) -> None:
        Rows, Cols = len(board), len(board[0])
        directions = [[1,0],[-1,0],[0,-1],[0,1]]

        def checkNeighbor(r,c):
            q=deque()
            board[r][c] = "Z"
            q.append((r,c))

            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    for dr, dc in directions:
                        nr, nc = row+dr, col+dc
                        if (nr<0 or nc<0 or nr==Rows or
                            nc==Cols or board[nr][nc]!= "O"):
                            continue
                        board[nr][nc] = "Z"
                        q.append((nr,nc))

        for r in range(Rows):
            if board[r][0] == "O":
                checkNeighbor(r,0)
            if board[r][Cols-1]== "O":                
                checkNeighbor(r,Cols-1)

        for c in range(Cols):
            if board[0][c]== "O":
                checkNeighbor(0, c)
            if board[Rows-1][c] == "O":
                checkNeighbor(Rows-1,c)

        for rw in range(Rows):
            for cl in range(Cols):
                if board[rw][cl] == "O":
                    board[rw][cl] = "X"
                if board[rw][cl] == "Z":
                    board[rw][cl] = "O"

        




