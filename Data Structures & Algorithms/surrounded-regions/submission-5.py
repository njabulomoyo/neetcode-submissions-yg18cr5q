class Solution:
    def solve(self, board: List[List[str]]) -> None:
        Rows, Cols = len(board), len(board[0])
        visited = set()
        q = deque()

        def dfs(r,c):
            if (r<0 or c<0 or r==Rows or
                c==Cols or (r,c) in visited
                or board[r][c] != "O"):
                return 

            visited.add((r,c))
            q.append((r,c))

        #Collecting the "O"s on the edge all sides
        for r in range(Rows):
            if board[r][0] == "O":
                q.append((r,0))
                visited.add((r,0))
            if board[r][Cols-1] == "O":
                q.append((r,Cols-1))
                visited.add((r,Cols-1))

        for c in range(Cols):
            if board[0][c] == "O":
                visited.add((0,c))
                q.append((0,c))
            if board[Rows-1][c] == "O":
                visited.add((Rows-1,c))
                q.append((Rows-1,c))
        #CHECKING ALL THE AFFECTED regions
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()

                dfs(row+1, col)
                dfs(row-1, col)
                dfs(row, col+1)
                dfs(row, col-1)
        #final check. marking surrounded regions with X
        for r in range(Rows):
            for c in range(Cols):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"







